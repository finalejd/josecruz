# Generated by Django 4.2.7 on 2023-11-05 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micrud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='nombreCiudad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='equipos',
            name='nombreEstadio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Ciudades',
        ),
        migrations.DeleteModel(
            name='Estadios',
        ),
    ]
