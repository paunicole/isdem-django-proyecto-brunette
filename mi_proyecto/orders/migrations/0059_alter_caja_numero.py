# Generated by Django 4.2.1 on 2023-12-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0058_alter_caja_fecha_hora_cierre_alter_caja_monto_final_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='numero',
            field=models.IntegerField(choices=[(1, 'Caja 1'), (2, 'Caja 2'), (3, 'Caja 3')]),
        ),
    ]
