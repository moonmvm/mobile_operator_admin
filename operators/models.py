from django.db import models

from utils.constants import REGION_TYPES


class Filial(models.Model):
    name = models.CharField(max_length=20)
    region = models.CharField(max_length=30, choices=REGION_TYPES)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return f'Filial: {self.name}. Region: {self.region}'


class FilialGadget(models.Model):
    amount = models.IntegerField()
    filial = models.ForeignKey(Filial, on_delete=models.PROTECT)
    gadget = models.ForeignKey('gadgets.Gadget', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Гаджеты в филиалах'

    def __str__(self):
        return f'Gadget: {self.gadget.name}. Operator: {self.filial.name}. Amount: {self.amount}'


class SoldGadget(models.Model):
    amount = models.IntegerField('Amounts')
    gadget = models.ForeignKey(FilialGadget, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Проданные гаджеты'

    def __str__(self):
        return f'Sold gadget: {self.gadget}. Date: {self.date}'

    def save(self, *args, **kwargs):
        if self.gadget.amount >= self.amount:
            self.gadget.amount -= self.amount
            self.gadget.save(update_fields=['amount'])
        else:
            raise Exception('Filial does not have enough gadgets')
        super(SoldGadget, self).save(*args, **kwargs)
