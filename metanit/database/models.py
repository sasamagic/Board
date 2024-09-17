from django.db import models

class Modules(models.Model):
    product_family = models.CharField(max_length=10)
    product_type = models.CharField(max_length=10)
    revision = models.IntegerField()
    serial_number = models.CharField(max_length=30, unique=True)
    sequence_number = models.IntegerField()
    manufacturer = models.CharField(max_length=10)
    date_of_production = models.IntegerField()
    history_of_module = models.CharField(max_length=10000)
    # добавьте другие поля, которые нужны
    class Meta:
        db_table = 'modules'
    def __str__(self):
        return self.serial_number