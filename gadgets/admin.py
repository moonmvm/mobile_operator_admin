from django.contrib import admin

from .models import Brand, Gadget


class GadgetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'type', 'brand')
    search_fields = ('pk', 'name', 'type')


admin.site.register(Brand)
admin.site.register(Gadget, GadgetAdmin)
