# Generated by Django 2.2.7 on 2021-05-15 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0002_soldgadget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FilialTariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_joined', models.IntegerField(default=0)),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tariffs', to='operators.Filial')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='filials', to='operators.Tariff')),
            ],
        ),
    ]