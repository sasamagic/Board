# Тут описана модель для хранения информации формы "Регистрация модуля"
from django.db import models
class reg(models.Model):
    ec_number = models.ForeignKey(
        'info_modules',  # Ссылка на модель info_modules
        on_delete=models.CASCADE,  # Удаление связанных записей при удалении связанных объектов
        related_name='regs',  # Опционально, если нужно обратное имя для связи
        verbose_name='Номер еЦ',
        to_field='info_ec_number',  # Ссылка на поле info_ec_number вместо id
        db_column='ec_number',  # Настройка названия столбца в базе данных
        default='еЦ_.___.___-__'
    )
    module_count = models.PositiveIntegerField(verbose_name='Количество изделий')
    production_date = models.DateField(verbose_name='Дата производства')
    history = models.TextField(max_length=10000, verbose_name='История изделия')
    number_of_module = models.PositiveIntegerField(verbose_name='Номер изделия')
    def str(self):
        return f"{self.ec_number} - {self.number_of_module}"  # Изменение в строковом представлении

class info_modules(models.Model):
    info_ec_number = models.CharField(max_length=100, verbose_name='Номер еЦ', unique=True, default='еЦ_.___.___-__')
    info_product_family = models.CharField(max_length=100, verbose_name='Семейство изделия')
    info_product_family_code = models.PositiveIntegerField(verbose_name='Код семейства изделия')
    info_revision = models.PositiveIntegerField(verbose_name='Ревизия')
    info_revision_code = models.PositiveIntegerField(verbose_name='Код ревизии')
    info_product_type = models.CharField(max_length=100, verbose_name='Тип изделия')
    info_product_type_code = models.PositiveIntegerField(verbose_name='Код типа изделия')
    info_manufacturer = models.CharField(max_length=100, verbose_name='Производитель')
    info_manufacturer_code = models.PositiveIntegerField(verbose_name='Код производителя')

    def str(self):
        return f"{self.info_ec_number} - {self.info_manufacturer_code}"

class Serial_Numbers(models.Model):
    combined_field = models.TextField(verbose_name='Объединенное поле', blank=True)

    def str(self):
        return self.combined_field
class SPP(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(verbose_name='Дата прохождения СПП')
    user_id = models.PositiveIntegerField(verbose_name='id пользователя')
    data = models.TextField(max_length=1000000, verbose_name='Текст лога с ошибков')
    file = models.TextField(max_length=1000000, verbose_name='Файл')
    def __str__(self):
        return f"{self.id} - {self.file}"  # Изменение в строковом представлении

