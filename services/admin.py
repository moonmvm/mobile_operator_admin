from django.contrib import admin

from . import models


class ConnectedTariffAdmin(admin.ModelAdmin):
    list_display = ('pk', 'filial', 'tariff', 'client')
    search_fields = ('filial__name', 'tariff__name', 'client__first_name')


class ConnectedTvAdmin(admin.ModelAdmin):
    list_display = ('pk', 'filial', 'tv', 'client')
    search_fields = ('filial__name', 'tv__name', 'client__first_name')


admin.site.register(models.Tariff)
admin.site.register(models.Tv)
admin.site.register(models.ConnectedTariff, ConnectedTariffAdmin)
admin.site.register(models.ConnectedTv, ConnectedTvAdmin)
