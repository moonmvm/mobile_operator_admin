from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class ServicesConfig(AppConfig):
    name = 'services'
    verbose_name = 'Услуги'

    def ready(self):
        autodiscover_modules('auditlog', 'signals')
