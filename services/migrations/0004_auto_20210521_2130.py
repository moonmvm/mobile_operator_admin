# Generated by Django 2.2.7 on 2021-05-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20210521_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectedtariff',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='connectedtv',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
