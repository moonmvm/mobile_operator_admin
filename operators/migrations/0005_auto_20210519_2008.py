# Generated by Django 2.2.7 on 2021-05-19 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0004_auto_20210517_1002'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FilialTariff',
        ),
        migrations.DeleteModel(
            name='Tariff',
        ),
    ]
