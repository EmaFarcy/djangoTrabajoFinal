# Generated by Django 4.0.3 on 2022-04-09 23:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_ruta_caracteristicas'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
