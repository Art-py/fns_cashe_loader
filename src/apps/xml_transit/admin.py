from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from apps.xml_transit.models import XMLFile, XSDSchema


class XSDSchemaAdmin(admin.ModelAdmin):
    list_display = ("id", "created_timestamp")
    list_display_links = list_display

    list_filter = (("created_timestamp", DateRangeFilter),)


class XMLFileAdmin(admin.ModelAdmin):
    list_display = ("id", "created_timestamp")
    list_display_links = list_display

    list_filter = (("created_timestamp", DateRangeFilter),)


admin.site.register(XSDSchema, XSDSchemaAdmin)
admin.site.register(XMLFile, XMLFileAdmin)
