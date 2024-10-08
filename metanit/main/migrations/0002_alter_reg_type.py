# Generated by Django 5.1.1 on 2024-09-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='type',
            field=models.CharField(choices=[('MU.1', 'Модуль МУ.1 еЦ5.155.01904'), ('MU.2', 'Модуль МУ.1 еЦ5.155.019-0104'), ('MU.3', 'Модуль МУ.3 еЦ5.155.02304'), ('MU.4', 'Модуль МУ.3 еЦ5.155.023-0104'), ('MVVS.1', 'Модуль МПД'), ('MVVS.2', 'Модуль МВД'), ('MVVS.3', 'Модуль МВД‑У'), ('MVVS.4', 'Модуль МПТ'), ('MVVS.5', 'Модуль МВА'), ('MVVS.6', 'Модуль МПА'), ('MVVS.7', 'Модуль МПИ‑У'), ('MVVS.8', 'Модуль МСР'), ('MVVS.9', 'Модуль МКА'), ('MVVS.10', 'Модуль МППТ'), ('MVVS.11', 'Модуль МПИ'), ('MR.1', 'Модуль МР'), ('MD.1', 'Модуль МД'), ('MVVS_SPIN.1', 'Модуль МК'), ('KP.1', 'Плата объединительная КП.1'), ('BOS.1', 'Блок БОС.1'), ('BOS.2', 'Блок БОС.2'), ('BOS.3', 'Модуль МОС.24'), ('BOS.4', 'Модуль МОС.25'), ('BV.1', 'Блок БВ.1еЦ5.139.14404'), ('BV.2', 'Блок БВ.1еЦ5.139.144-0104'), ('BV.3', 'Блок БВ.1еЦ5.139.144-0204'), ('BV.4', 'Блок БВ.1еЦ5.139.144-0304'), ('SK.1', 'Соединитель клеммный СКеЦ5.282.24204'), ('SK.2', 'Соединитель клеммный СКАеЦ5.282.25104'), ('SK.3', 'Соединитель клеммный СКА‑УеЦ5.282.25304'), ('SK.4', 'Соединитель клеммный СКПИеЦ5.282.24404'), ('SK.5', 'Соединитель клеммный СКПИ.2еЦ5.282.26704'), ('SK.6', 'Соединитель клеммный СКТДеЦ5.282.25204'), ('SK.7', 'Соединитель клеммный СКДАеЦ5.282.24804'), ('SK.8', 'Соединитель клеммный СКДДеЦ5.282.24704'), ('SK.9', 'Соединитель клеммный СКДРеЦ5.282.25004'), ('SK.10', 'Соединитель клеммный СКИМеЦ5.282.26104'), ('SK.11', 'Соединитель клеммный СК‑МСРеЦ5.282.26604'), ('SK.12', 'Соединитель клеммный СКД‑МСРеЦ5.282.26504'), ('SK.13', 'Соединитель клеммный СК‑МКАеЦ5.282.25404'), ('SK.14', 'Соединитель клеммный СКД‑МКАеЦ5.282.25504'), ('SK.15', 'Соединитель клеммный СКНеЦ5.282.24904'), ('KABELS.1', 'Кабель КАСеЦ6.641.73304'), ('KABELS.2', 'Кабель КАСеЦ6.641.733-0104'), ('KONSTRUCTIVEELEMINT.1', 'Каркас объединительный КО.1'), ('KONSTRUCTIVEELEMINT.2', 'Заглушка еЦ6.433.069'), ('KONSTRUCTIVEELEMINT.3', 'Заглушка еЦ6.433.070')], max_length=255, verbose_name='Тип'),
        ),
    ]
