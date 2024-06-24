from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedAbstractModel
from apps.common.services import prefix_based_upload_handler


class XSDSchema(TimeStampedAbstractModel):
    # Main fields
    xsd_schema = models.FileField(
        verbose_name=_("xsd schema"),
        upload_to=prefix_based_upload_handler("files/xml_transit/xsd_schemas"),
    )

    # Unnecessary fields
    updated_timestamp = None

    class Meta:
        verbose_name = _("xsd schema")
        verbose_name_plural = _("xsd schemas")


class XMLFile(TimeStampedAbstractModel):
    # Main fields
    xml_file = models.FileField(
        verbose_name=_("xml file"),
        upload_to=prefix_based_upload_handler("files/xml_transit/xml_file"),
    )

    # Unnecessary fields
    updated_timestamp = None

    class Meta:
        verbose_name = _("xml file")
        verbose_name_plural = _("xml files")
