# Generated by Django 5.1.1 on 2024-10-29 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modules',
            name='product_family',
        ),
    ]