from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUserModel

class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ['id', 'email', 'name', 'user_type', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'name']
    ordering = ['id', 'name']
    readonly_fields = ['last_login']

    fieldsets = (
        (
            None, {
                'fields': ( 'user_type', 'email', 'name', 'password')
            }
        ),
        (
            'permissions', {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            }
        ),
        (
            'Important dates', {
                'fields':('last_login', ),
            }
        )
    )

    add_fieldsets = (
    (
        None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'user_type', 'password1', 'password2')
        }
    ),
    (
        'Permissions', {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }
    ),
)

admin.site.register(CustomUserModel, CustomAdmin)