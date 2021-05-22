# Generated by Django 2.2.7 on 2021-05-14 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(choices=[('Smartphone', 'Smartphone'), ('Tablet', 'Tablet'), ('Headphones', 'Headphones'), ('Smart watch', 'Smart watch'), ('Portable speaker', 'Portable speaker')], max_length=20)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gadgets.Brand')),
            ],
        ),
    ]