from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomModelManager(BaseUserManager):

    def create_user(self, email, name, user_type = 'customer', password = None, **extra_fields):
        if not email:
            raise ValueError("User must have an email...")
        
        email = self.normalize_email(email)
        user = self.model(email= email, name = name, user_type = user_type, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, name, user_type = 'admin', password = None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, name, user_type, password, **extra_fields)

class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    
    USER_TYPE = (
        ('customer', 'CUSTOMER'),
        ('seller', 'SELLER'),
        ('admin', 'ADMIN'),
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomModelManager()

    def get_email(self):
        return self.email
    
    def get_name(self):
        return self.name