from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from apps.common.admin import SearchHelpTextMixin
from apps.xml_transit.models import XSDSchema


class XSDSchemaAdmin(admin.ModelAdmin, SearchHelpTextMixin):
    list_display = ("id", "type", "created_timestamp")
    list_display_links = list_display

    search_fields = ("folder_name",)

    list_filter = (("created_timestamp", DateRangeFilter), "type")


admin.site.register(XSDSchema, XSDSchemaAdmin)
