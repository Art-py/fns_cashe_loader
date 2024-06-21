from celery import shared_task

from apps.xml_transit.services.exemple import exemple_service


@shared_task(name="xml_transit.transit_xml_to_database")
def transit_xml_to_database() -> None:
    exemple_service()
    print("asd1223333333333333333333")
