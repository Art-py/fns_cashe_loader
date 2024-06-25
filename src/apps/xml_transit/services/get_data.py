from xmlschema import XMLSchema

from apps.xml_transit.models import XMLFile, XSDSchema


class XMLProcessor:

    @staticmethod
    def _get_last_xsd_path() -> str:
        return XSDSchema.objects.all().order_by("created_timestamp").last().xsd_schema.path

    @staticmethod
    def _get_last_xml_path() -> str:
        return XMLFile.objects.all().order_by("created_timestamp").last().xml_file.path

    def get_data_from_xml(self):
        xsd_path = self._get_last_xsd_path()
        xml_path = self._get_last_xml_path()

        schema = XMLSchema(xsd_path)
        is_valid = schema.is_valid(xml_path)
        if is_valid:
            return schema.to_dict(xml_path)
