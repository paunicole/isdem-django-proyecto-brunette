# Generated by Django 4.2.1 on 2023-12-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0050_rename_id_caja_caja_empleado_caja_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='fecha_apertura',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='caja',
            name='fecha_cierre',
            field=models.DateTimeField(),
        ),
    ]
