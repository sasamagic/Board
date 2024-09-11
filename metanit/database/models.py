# models.py

from django.db import models

class Module(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    # Добавьте другие поля, если необходимо

    def __str__(self):
        return self.serial_number
