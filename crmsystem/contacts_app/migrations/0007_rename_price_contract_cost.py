# Generated by Django 5.1.3 on 2024-12-07 13:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts_app", "0006_rename_creation_data_contract_end_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contract",
            old_name="price",
            new_name="cost",
        ),
    ]
