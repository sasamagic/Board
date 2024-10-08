# Тут описана модель для хранения информации формы "Регистрация модуля"
from django.db import models

class reg(models.Model):
    ec_number = models.CharField(max_length=100, default='')
    module_count = models.PositiveIntegerField(verbose_name='Количество модулей')
    production_date = models.DateField(verbose_name='Дата производства')
    history = models.TextField(max_length=10000, verbose_name='История модуля')

    def __str__(self):
        return f"{self.ec_number} - {self.module_count}"  # Изменение в строковом представлении

class info_modules(models.Model):
    info_ec_number = models.CharField(max_length=100, default='Номер еЦ')
    info_product_family = models.CharField(max_length=100, verbose_name='Семейство продукта')
    info_revision = models.PositiveIntegerField(verbose_name='Ревизия')
    info_product_type = models.CharField(max_length=100, verbose_name='Тип продукта')
    info_manufacturer = models.CharField(max_length=100, verbose_name='Производитель')
    info_manufacturer_code = models.PositiveIntegerField(verbose_name='Код производителя')
    info_product_type_code = models.PositiveIntegerField(verbose_name='Код типа продукта')
    info_revision_code = models.PositiveIntegerField(verbose_name='Код ревизии')
    def __str__(self):
        return f"{self.info_ec_number} - {self.info_product_family}"
