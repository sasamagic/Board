# Generated by Django 5.1.1 on 2024-10-29 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_kalibrovka_serial_number_poverka_serial_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proverka',
            name='serial_number',
            field=models.ForeignKey(db_column='serial_number', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.serial_numbers', to_field='combined_field', verbose_name='Серийный номер'),
        ),
    ]
