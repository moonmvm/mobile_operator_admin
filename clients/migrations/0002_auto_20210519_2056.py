# Generated by Django 2.2.7 on 2021-05-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]