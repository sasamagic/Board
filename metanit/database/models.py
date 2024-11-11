# # # # Тут описана модель для хранения полной информации о модулях
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import reg, Serial_Numbers, info_modules

class Modules(models.Model):
    product_family = models.ForeignKey(
        'main.info_modules',
        on_delete=models.CASCADE,
        verbose_name='Семейство изделия',
        null=True,
        related_name='modules_product_family'
    )
    product_type = models.ForeignKey(
        'main.info_modules',
        on_delete=models.CASCADE,
        verbose_name='Тип продукта',
        null=True,
        related_name='modules_product_type'
    )
    revision = models.ForeignKey(
        'main.info_modules',
        on_delete=models.CASCADE,
        verbose_name='Ревизия',
        null=True,
        related_name='modules_revision'
    )
    serial_number = models.ForeignKey(
        'main.Serial_Numbers',
        on_delete=models.CASCADE,
        verbose_name='Серийный номер',
        null=True,
        related_name='modules_serial_number'
    )
    sequence_number = models.ForeignKey(
        'main.reg',
        on_delete=models.CASCADE,
        verbose_name='Номер изделия',
        null=True,
        related_name='modules_sequence_number'
    )
    manufacturer = models.ForeignKey(
        'main.info_modules',
        on_delete=models.CASCADE,
        verbose_name='Производитель',
        null=True,
        related_name='modules_manufacturer'
    )
    number_ec = models.ForeignKey(
        'main.reg',
        on_delete=models.CASCADE,
        verbose_name='Номер еЦ',
        null=True,
        related_name='modules_number_ec'
    )
    date_of_production = models.ForeignKey(
        'main.reg',
        on_delete=models.CASCADE,
        verbose_name='Дата производства',
        null=True,
        related_name='modules_date_of_production'
    )
    history_of_module = models.ForeignKey(
        'main.reg',
        on_delete=models.CASCADE,
        verbose_name='История изделия',
        null=True,
        related_name='modules_history_of_module'
    )

    # Методы отображения остаются такими же
    def __str__(self):
        return f"{self.product_family} - {self.history_of_module}"

    # Обработчик для обновления или создания записи в Modules при сохранении reg
    @receiver(post_save, sender=reg)
    def update_modules_from_reg(sender, instance, created, **kwargs):
        module_entry, _ = Modules.objects.get_or_create(
            sequence_number=instance
        )
        module_entry.number_ec = instance
        module_entry.date_of_production = instance
        module_entry.history_of_module = instance
        module_entry.save()

    # Обработчик для обновления или создания записи в Modules при сохранении Serial_Numbers
    @receiver(post_save, sender=Serial_Numbers)
    def update_modules_from_serial_numbers(sender, instance, created, **kwargs):
        module_entry, _ = Modules.objects.get_or_create(
            serial_number=instance
        )
        module_entry.serial_number = instance
        module_entry.save()

    # Обработчик для обновления или создания записи в Modules при сохранении info_modules
    @receiver(post_save, sender=info_modules)
    def update_modules_from_info_modules(sender, instance, created, **kwargs):
        module_entry, _ = Modules.objects.get_or_create(
            product_family=instance
        )
        module_entry.product_family = instance
        module_entry.product_type = instance
        module_entry.revision = instance
        module_entry.manufacturer = instance
        module_entry.save()
