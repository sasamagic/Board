# Generated by Django 5.1.1 on 2024-09-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_modules_regi_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regi',
            name='module_count',
            field=models.PositiveIntegerField(verbose_name='Количество модулей'),
        ),
    ]
