# Generated by Django 4.0.3 on 2022-04-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_ruta'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='caracteristicas',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
