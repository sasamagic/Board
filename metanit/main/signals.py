# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import reg, info_modules, Serial_Numbers
#
# @receiver(post_save, sender=reg)
# def match_and_save(sender, instance, **kwargs):
#     if instance.ec_number:
#         matching_modules = info_modules.objects.filter(info_ec_number=instance.ec_number.info_ec_number)
#
#         for module in matching_modules:
#             # Создаем объединённую строку из данных модуля и экземпляра reg
#             combined_info = f"00:" \
#                             f"{module.info_manufacturer_code}:" \
#                             f"{module.info_product_family_code}" \
#                             f"{module.info_product_type_code}:" \
#                             f"{module.info_revision_code}:" \
#                             f"{instance.production_date}:" \
#                             f"{instance.number_of_module}"
#
#             # Создаем или обновляем запись в Serial_Numbers
#             Serial_Numbers.objects.update_or_create(
#                 combined_field=combined_info,
#             )
#     else:
#         print("Ошибка: ec_number не найден.")
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import reg, info_modules, Serial_Numbers

@receiver(post_save, sender=reg)
def match_and_save(sender, instance, **kwargs):
    if instance.ec_number:
        matching_modules = info_modules.objects.filter(info_ec_number=instance.ec_number.info_ec_number)

        for module in matching_modules:
            # Преобразуем дату в формат "номер недели + год" (например, 2524)
            production_date = instance.production_date
            week_number = production_date.isocalendar()[1]  # Получаем номер недели
            year = production_date.year  # Получаем год

            # Формируем строку в нужном формате, без разделителей
            week_year_format = f"{week_number:02}{str(year)[-2:]}"  # Номер недели (2 цифры) + последние 2 цифры года

            # Создаем объединённую строку из данных модуля и экземпляра reg
            combined_info = f"00:" \
                            f"{module.info_manufacturer_code}:" \
                            f"{module.info_product_family_code}:" \
                            f"{module.info_product_type_code}:" \
                            f"{module.info_revision_code}:" \
                            f"{week_year_format}:" \
                            f"{instance.number_of_module}"

            # Создаем или обновляем запись в Serial_Numbers
            Serial_Numbers.objects.update_or_create(
                combined_field=combined_info,
            )
    else:
        print("Ошибка: ec_number не найден.")