from django.contrib import admin

from . import models


class FilialAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'street', 'house')
    search_fields = ('name', 'region', 'street', 'house')


class FilialGadgetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'filial', 'gadget', 'amount', 'price', 'available')
    search_fields = ('filial__name', 'gadget__name')


class SoldGadgetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'amount', 'gadget', 'date')
    search_fields = ('pk', 'date')
    list_filter = ('gadget__gadget__name',)


admin.site.register(models.Filial, FilialAdmin)
admin.site.register(models.FilialGadget, FilialGadgetAdmin)
admin.site.register(models.SoldGadget, SoldGadgetAdmin)
