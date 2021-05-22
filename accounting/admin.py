from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from .models import Accounting, AccountingOperation
from . import services


class AccountingAdmin(admin.ModelAdmin):
    change_list_template = 'accounting_changelist.html'
    list_display = (
        'operation',
        'yesterday',
        'today',
        'previous_week',
        'current_week',
        'previous_month',
        'current_month',
    )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('calculate-accounting/', self.calculate_accounting),
        ]
        return my_urls + urls

    def calculate_accounting(self, request):
        services.calculate_accounting()
        self.message_user(request, "Calculated!")
        return HttpResponseRedirect("../")


class AccountingOperationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'price', 'operation', 'date')
    search_fields = ('price', 'operation')


admin.site.register(Accounting, AccountingAdmin)
admin.site.register(AccountingOperation, AccountingOperationAdmin)
