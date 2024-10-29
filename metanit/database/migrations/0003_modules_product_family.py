# Generated by Django 5.1.1 on 2024-10-29 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_remove_modules_product_family'),
        ('main', '0007_alter_proverka_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='product_family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.info_modules', verbose_name='Семейство изделия'),
        ),
    ]