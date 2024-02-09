from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Commissionaire


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personnal Info'), {'fields': ('full_name', 'phone', 'gender', 'birthday', 'profile')}),
        (('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (('Importants dates'), {'fields': ('last_login', 'date_joined')}),
    )

    """For new User"""
    add_fieldsets =(
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    ) 
    list_display = ('email', 'full_name', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Commissionaire)
