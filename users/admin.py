from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'last_login', 'date_joined'),
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name'),
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff', 'is_active', 'groups'),
        }),
    )
    list_display = ('pk', 'email', 'is_superuser', 'last_login', 'date_joined')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('pk',)


admin.site.register(User, CustomUserAdmin)
