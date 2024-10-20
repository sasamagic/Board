from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import reg, info_modules, Serial_Numbers

# @receiver(post_save, sender=reg)
# def match_and_save(sender, instance, **kwargs):
#     # Поиск всех записей в info_modules, у которых совпадает info_ec_number с ec_number
#     matching_modules = info_modules.objects.filter(info_ec_number=instance.ec_number.info_ec_number)
#
#     # Если совпадение найдено, создаем или обновляем запись в Serial_Numbers
#     for module in matching_modules:
#         Serial_Numbers.objects.update_or_create(
#             ser_info_manufacturer_code=module.info_manufacturer_code,
#             ser_info_product_family_code=module.info_product_family_code,
#             ser_info_product_type_code=module.info_product_type_code,
#             ser_info_revision_code=module.info_revision_code,
#             ser_production_date=instance.production_date,
#             ser_number_of_module=instance.number_of_module,
#         )
@receiver(post_save, sender=reg)
def match_and_save(sender, instance, **kwargs):
    # Убедитесь, что instance.ec_number возвращает объект info_modules
    if instance.ec_number:
        matching_modules = info_modules.objects.filter(info_ec_number=instance.ec_number.info_ec_number)

        # Если совпадение найдено, создаем или обновляем запись в Serial_Numbers
        for module in matching_modules:
            Serial_Numbers.objects.update_or_create(
                ser_info_manufacturer_code=module.info_manufacturer_code,
                ser_info_product_family_code=module.info_product_family_code,
                ser_info_product_type_code=module.info_product_type_code,
                ser_info_revision_code=module.info_revision_code,
                ser_production_date=instance.production_date,
                ser_number_of_module=instance.number_of_module,
            )
    else:
        print("Ошибка: ec_number не найден.")