# Generated by Django 5.1.3 on 2024-12-03 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services_app", "0002_alter_services_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("file", models.FileField(upload_to="files/")),
                ("creation_data", models.DateTimeField(auto_now_add=True)),
                ("expire_date", models.DateTimeField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "provided_service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services_app.services",
                    ),
                ),
            ],
        ),
    ]
