# Generated by Django 2.2.7 on 2021-05-20 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_auto_20210520_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acccuntingoperation',
            name='tv',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='accounting_operations', to='services.ConnectedTv'),
        ),
    ]
