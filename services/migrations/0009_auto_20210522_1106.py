# Generated by Django 2.2.7 on 2021-05-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20210522_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectedtariff',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='connectedtv',
            name='date',
            field=models.DateField(),
        ),
    ]