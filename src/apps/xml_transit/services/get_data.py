import os
import tempfile
import zipfile
from datetime import date, timedelta

from bs4 import BeautifulSoup
from django.conf import settings
from requests import Session
from requests_pkcs12 import Pkcs12Adapter, get
from xmlschema import XMLSchema

from apps.xml_transit.choices import XSDSchemaType
from apps.xml_transit.models import XSDSchema


class XMLProcessor:

    @staticmethod
    def _get_last_xsd(xsd_type: XSDSchemaType) -> XSDSchema:
        return XSDSchema.objects.filter(type=xsd_type).order_by("created_timestamp").last()

    @staticmethod
    def _get_yesterdays_date() -> str:
        previous_date = date.today() - timedelta(days=1)
        return previous_date.strftime("%d.%m.%Y")

    def _get_path_to_zip(self, xsd_schema: XSDSchema) -> str:
        response = get(
            f"{settings.FTP_HOST}/?dir={xsd_schema.folder_name}/{self._get_yesterdays_date()}/",
            pkcs12_filename=settings.FTP_CERT,
            pkcs12_password=settings.FTP_PASS,
        )

        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("li"):
            if isinstance(link.get("data-href"), str) and ".zip" in link.get("data-href"):
                return f'{settings.FTP_HOST}/{link.get("data-href")}/'

    @staticmethod
    def _download_zip(path_to_zip: str, session: Session) -> str:
        r = session.get(path_to_zip)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as temp_file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    temp_file.write(chunk)
            temp_zip_path = temp_file.name

        return temp_zip_path

    @staticmethod
    def _extract_files_from_zip(temp_zip_path: str):
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(temp_zip_path, "r") as zip_ref:
                zip_ref.extractall(temp_dir)

            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    yield file_path

        os.remove(temp_zip_path)

    def _get_xml(self, xsd_schema: XSDSchema):
        with Session() as s:
            s.mount(
                settings.FTP_HOST,
                Pkcs12Adapter(pkcs12_filename=settings.FTP_CERT, pkcs12_password=settings.FTP_PASS),
            )

            path = self._get_path_to_zip(xsd_schema=xsd_schema)
            temp_zip_path = self._download_zip(path_to_zip=path, session=s)
            yield self._extract_files_from_zip(temp_zip_path=temp_zip_path)

    def get_data_from_xml(self, xsd_type: XSDSchemaType):
        xsd_schema = self._get_last_xsd(xsd_type=xsd_type)
        schema = XMLSchema(xsd_schema.xsd_schema.path)

        data_list = []
        for temp_file_path in self._get_xml(xsd_schema=xsd_schema):
            is_valid = schema.is_valid(temp_file_path)
            if is_valid:
                data_list.append(schema.to_dict(temp_file_path))
            os.remove(temp_file_path)
        return data_list
