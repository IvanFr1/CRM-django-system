# Generated by Django 5.1.3 on 2024-12-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0003_alter_contract_creation_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='creation_data',
            field=models.DateTimeField(),
        ),
    ]