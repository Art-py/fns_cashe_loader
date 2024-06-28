from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedAbstractModel
from apps.common.services import prefix_based_upload_handler
from apps.xml_transit.choices import XSDSchemaType


class XSDSchema(TimeStampedAbstractModel):
    # Main fields
    xsd_schema = models.FileField(
        verbose_name=_("xsd schema"),
        upload_to=prefix_based_upload_handler("files/xml_transit/xsd_schemas"),
    )
    folder_name = models.CharField(verbose_name=_("folder name"), max_length=100)
    type = models.PositiveSmallIntegerField(verbose_name=_("type"), choices=XSDSchemaType.choices)

    # Unnecessary fields
    updated_timestamp = None

    class Meta:
        verbose_name = _("xsd schema")
        verbose_name_plural = _("xsd schemas")
