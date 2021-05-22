# Generated by Django 2.2.7 on 2021-05-15 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldGadget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('gadget', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='operators.FilialGadget')),
            ],
        ),
    ]