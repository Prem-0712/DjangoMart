from django.contrib import admin
from .models import CustomerModel

@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'address', 'phone_number']