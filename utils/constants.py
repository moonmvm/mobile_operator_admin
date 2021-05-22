from enum import Enum

from .factories_utils import enum_choices_factory


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class AccountingOperation(AutoName):
    TV_CONNECTED = 'Подключено телевидение'
    TARIFF_CONNECTED = 'Подключен тариф'
    GADGET_SOLD = 'Продан гаджет'


class Gadget(AutoName):
    LAPTOP = 'Ноутбук'
    SMARTPHONE = 'Смартфон'
    TABLET = 'Планшет'
    HEADPHONES = 'Наушники'
    SMART_WATCH = 'Умные часы'
    PORTABLE = 'Портативная колонка'


class Region(AutoName):
    BREST = 'Брестская область'
    VITEBSK = 'Витебская область'
    GOMEL = 'Гомельская область'
    GRODNO = 'Гродненская область'
    MINSK = 'Минская область'
    MINSK_CITY = 'Минск'


ACCOUNTING_OPERATIONS = enum_choices_factory(AccountingOperation)
GADGET_TYPES = enum_choices_factory(Gadget)
REGION_TYPES = enum_choices_factory(Region)
