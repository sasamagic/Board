# Тут описана модель для хранения полной информации о модулях

from django.db import models

class Modules(models.Model):
    # product_family = models.CharField(max_length=10)
    product_family = models.ForeignKey(
        'main.info_modules',  # Ссылка на модель info_modules
        on_delete=models.CASCADE,  # Удаление связанных записей при удалении связанных объектов
        verbose_name='Семейство изделия',
        null=True
    )
    # product_type = models.CharField(max_length=10)
    # revision = models.IntegerField()
    # serial_number = models.CharField(max_length=30, unique=True)
    # sequence_number = models.IntegerField()
    # manufacturer = models.CharField(max_length=10)
    # date_of_production = models.IntegerField()
    # history_of_module = models.CharField(max_length=10000)
    product_type = models.ForeignKey(
        'main.info_product_type',  # Ссылка на модель info_modules
        on_delete=models.CASCADE,  # Удаление связанных записей при удалении связанных объектов
        verbose_name='Тип продукта',
        null=True
    )
    product_type = models.ForeignKey(
        'main.info_product_type',  # Ссылка на модель info_modules
        on_delete=models.CASCADE,  # Удаление связанных записей при удалении связанных объектов
        verbose_name='Тип продукта',
        null=True
    )
    # добавьте другие поля, которые нужны
    # Добавляем вычисляемое свойство для отображения значения info_product_family
    @property
    def product_family_display(self):
        return self.product_family.info_product_family  # Получение значения из связанной модели
    def __str__(self):
        return self.serial_number



