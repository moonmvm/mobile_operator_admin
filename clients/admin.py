from django.contrib import admin

from . import models


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'phone',
        'date_of_birth',
    )


admin.site.register(models.Client, ClientAdmin)
