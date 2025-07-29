from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.db import models

class CustomerModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(unique=True)

    address = models.TextField()
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=10)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.user.name} - {self.user.email} - {self.name}'