from django.db import models

from utils.constants import ACCOUNTING_OPERATIONS


class Accounting(models.Model):
    operation = models.CharField(max_length=50, choices=ACCOUNTING_OPERATIONS, unique=True)
    yesterday = models.PositiveIntegerField(blank=True, null=True)
    today = models.PositiveIntegerField(blank=True, null=True)
    previous_week = models.PositiveIntegerField(blank=True, null=True)
    current_week = models.PositiveIntegerField(blank=True, null=True)
    previous_month = models.PositiveIntegerField(blank=True, null=True)
    current_month = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Бухгалтерия'

    def __str__(self):
        return 'Operation: {}. By today: {}. By week: {}. By month: {}.'.format(
            self.operation, self.today, self.current_week, self.current_month,
        )


class AccountingOperation(models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2)
    operation = models.CharField(max_length=50, choices=ACCOUNTING_OPERATIONS)
    gadget = models.OneToOneField(
        'operators.SoldGadget',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='accounting_operations',
    )
    tariff = models.OneToOneField(
        'services.ConnectedTariff',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='accounting_operations',
    )
    tv = models.OneToOneField(
        'services.ConnectedTv',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='accounting_operations',
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Бухгалтерские операции'

    def __str__(self):
        return f'Operation: {self.operation}. Amount: {self.price}. Date: {self.date}'
