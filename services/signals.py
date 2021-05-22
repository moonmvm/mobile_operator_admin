from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ConnectedTariff, ConnectedTv
from accounting.models import AccountingOperation
from utils.constants import AccountingOperation as Operation


@transaction.atomic
@receiver(post_save, sender=ConnectedTv)
def create_tv_accounting_operation(sender, created, instance, **kwargs):
    if created:
        AccountingOperation.objects.create(
            price=instance.tv.price,
            operation=Operation.TV_CONNECTED.value,
            tv=instance,
        )


@transaction.atomic
@receiver(post_save, sender=ConnectedTariff)
def create_tariff_accounting_operation(sender, created, instance, **kwargs):
    if created:
        AccountingOperation.objects.create(
            price=instance.tariff.price,
            operation=Operation.TARIFF_CONNECTED.value,
            tariff=instance,
        )
