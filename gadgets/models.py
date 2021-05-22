from django.db import models

from utils.constants import GADGET_TYPES


class Brand(models.Model):
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return f'Brand: {self.name}'


class Gadget(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=20, choices=GADGET_TYPES)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Гаджеты'

    def __str__(self):
        return f'Gadget: {self.name}. Type: {self.type}. Brand: {self.brand}'
