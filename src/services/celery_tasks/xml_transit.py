from celery import shared_task

from apps.xml_transit.services.get_data import XMLProcessor


@shared_task(name="xml_transit.transit_xml_to_database")
def transit_xml_to_database() -> None:
    data = XMLProcessor().get_data_from_xml()
