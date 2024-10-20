# Generated by Django 5.1.1 on 2024-10-20 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_reg_number_of_module_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serial_Numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_info_manufacturer_code', models.PositiveIntegerField(verbose_name='Код производителя')),
                ('ser_info_product_family_code', models.PositiveIntegerField(verbose_name='Код семейства изделия')),
                ('ser_info_product_type_code', models.PositiveIntegerField(verbose_name='Код типа изделия')),
                ('ser_info_revision_code', models.PositiveIntegerField(verbose_name='Код ревизии')),
                ('ser_production_date', models.DateField(verbose_name='Дата производства')),
                ('ser_number_of_module', models.PositiveIntegerField(verbose_name='Номер изделия')),
            ],
        ),
        migrations.AlterField(
            model_name='info_modules',
            name='info_ec_number',
            field=models.CharField(default='еЦ', max_length=100, verbose_name='Номер еЦ'),
        ),
        migrations.AlterField(
            model_name='reg',
            name='ec_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regs', to='main.info_modules', verbose_name='Номер еЦ'),
        ),
    ]
