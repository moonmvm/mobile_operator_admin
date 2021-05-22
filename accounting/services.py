# Copyright (c) 2019 Celadon Development LLC, All rights reserved.
# Author Dmitry Mishuto <dmitry.mishuto@celadon.ae>

from django.db import transaction

from .models import Accounting, AccountingOperation
from utils import constants, date_utils

OPERATIONS = constants.AccountingOperation


def reset_accounting_values(obj):
    obj.yesterday = 0
    obj.today = 0
    obj.previous_week = 0
    obj.current_week = 0
    obj.previous_month = 0
    obj.current_month = 0


def calculate_accounting_by_dates(obj, operation):
    reset_accounting_values(obj)
    yesterday_start, yesterday_end = date_utils.get_yesterday_start_and_end_time()
    today_start, today_end = date_utils.get_today_start_and_end_time()
    last_week_start, last_week_end = date_utils.get_last_week()
    week_start, week_end = date_utils.get_current_week()
    last_month_start, last_month_end = date_utils.get_last_month()
    month_start, month_end = date_utils.get_current_month()

    entries = AccountingOperation.objects.filter(operation=operation)

    yesterday_entries = entries.filter(date__range=[yesterday_start, yesterday_end])
    today_entries = entries.filter(date__range=[today_start, today_end])
    last_week_entries = entries.filter(date__range=[last_week_start, last_week_end])
    week_entries = entries.filter(date__range=[week_start, week_end])
    last_month_entries = entries.filter(date__range=[last_month_start, last_month_end])
    month_entries = entries.filter(date__range=[month_start, month_end])

    for entry in yesterday_entries:
        obj.yesterday += entry.price
    for entry in today_entries:
        obj.today += entry.price
    for entry in last_week_entries:
        obj.previous_week += entry.price
    for entry in week_entries:
        obj.current_week += entry.price
    for entry in last_month_entries:
        obj.previous_month += entry.price
    for entry in month_entries:
        obj.current_month += entry.price
    obj.save()


@transaction.atomic
def calculate_accounting():
    tariffs, _ = Accounting.objects.get_or_create(operation=OPERATIONS.TARIFF_CONNECTED.value)
    tvs, _ = Accounting.objects.get_or_create(operation=OPERATIONS.TV_CONNECTED.value)

    calculate_accounting_by_dates(tariffs, OPERATIONS.TARIFF_CONNECTED.value)
    calculate_accounting_by_dates(tvs, OPERATIONS.TV_CONNECTED.value)
