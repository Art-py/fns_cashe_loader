from django.db import models
from django.utils.translation import gettext_lazy as _


class XSDSchemaType(models.IntegerChoices):
    INDIVIDUAL_ENTREPRENEUR = 0, _("individual entrepreneur")
    LEGAL_ENTITY = 1, _("legal entity")
