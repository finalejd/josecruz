# Generated by Django 4.2.7 on 2023-11-05 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micrud', '0004_remove_equipos_numero_alter_equipos_numequipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='numEquipo',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
