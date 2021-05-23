from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import SoldGadget
from accounting.models import AccountingOperation
from utils.constants import AccountingOperation as Operation


@transaction.atomic
@receiver(post_save, sender=SoldGadget)
def add_sold_gadget_to_acccounting(sender, created, instance, **kwargs):
    if created:
        AccountingOperation.objects.create(
            price=instance.profit,
            operation=Operation.GADGET_SOLD.value,
            gadget=instance,
        )
