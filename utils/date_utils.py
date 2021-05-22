from datetime import date, datetime, time, timedelta
from typing import Tuple


def get_yesterday_start_and_end_time() -> Tuple[datetime, datetime]:
    """
    The function returns the start and the end of the current day.
    """
    today = datetime.now().date()
    yesterday = today - timedelta(1)
    start_date = datetime.combine(yesterday, time())
    end_date = datetime.combine(today, time())
    return start_date, end_date


def get_today_start_and_end_time() -> Tuple[datetime, datetime]:
    """
    The function returns the start and the end of the current day.
    """
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    return today_start, today_end


def get_last_week() -> Tuple[datetime, datetime]:
    """
    The function returns the first and last days of the last week.
    """
    now = date.today()
    last_day = now - timedelta(days=now.weekday())
    first_day = last_day - timedelta(days=6)
    end_date = datetime(last_day.year, last_day.month, last_day.day)
    start_date = datetime(first_day.year, first_day.month, first_day.day)
    return start_date, end_date


def get_current_week() -> Tuple[datetime, datetime]:
    """
    The function returns the first and last days of the current week.
    """
    now = date.today()
    start_day = now - timedelta(days=now.weekday())
    end_day = start_day + timedelta(days=6)
    start_date = datetime(start_day.year, start_day.month, start_day.day)
    end_date = datetime(end_day.year, end_day.month, end_day.day) + timedelta(1)
    return start_date, end_date


def get_last_month() -> Tuple[datetime, datetime]:
    """
    The function returns the first and last days of the last month.
    """
    now = datetime.now()
    year, month = now.year, now.month
    if month == 1:
        year -= 1
        month = 12
        start_date = datetime(year, month, 1)
    else:
        start_date = datetime(year, month - 1, 1)
    end_date = datetime(year, month, 1)
    return start_date, end_date


def get_current_month() -> Tuple[datetime, datetime]:
    """
    The function returns the first and last days of the current month.
    """
    now = datetime.now()
    year, month = now.year, now.month
    start_date = datetime(year, month, 1)
    if month == 12:
        year += 1
        month = 1
    end_date = datetime(year, month + 1, 1)
    return start_date, end_date


def get_current_year() -> Tuple[datetime, datetime]:
    """
    The function returns the first and last days of the current year.
    """
    now = datetime.now()
    year = now.year
    start_date = datetime(year, 1, 1)
    end_date = datetime(year + 1, 1, 1)
    return start_date, end_date
