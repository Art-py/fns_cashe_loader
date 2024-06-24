# Generated by Django 5.0.6 on 2024-06-24 13:57

import apps.common.services
import functools
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="XMLFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "xml_file",
                    models.FileField(
                        upload_to=functools.partial(
                            apps.common.services.upload_file_handler_path,
                            *("files/xml_transit/xml_file",),
                            **{}
                        ),
                        verbose_name="xml file",
                    ),
                ),
            ],
            options={
                "verbose_name": "xml file",
                "verbose_name_plural": "xml files",
            },
        ),
        migrations.CreateModel(
            name="XSDSchema",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "xsd_schema",
                    models.FileField(
                        upload_to=functools.partial(
                            apps.common.services.upload_file_handler_path,
                            *("files/xml_transit/xsd_schemas",),
                            **{}
                        ),
                        verbose_name="xsd schema",
                    ),
                ),
            ],
            options={
                "verbose_name": "xsd schema",
                "verbose_name_plural": "xsd schemas",
            },
        ),
    ]