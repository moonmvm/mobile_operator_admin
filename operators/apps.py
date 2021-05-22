from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class OperatorsConfig(AppConfig):
    name = 'operators'
    verbose_name = 'Оператор'

    def ready(self):
        autodiscover_modules('signals')
