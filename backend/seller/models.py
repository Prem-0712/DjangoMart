from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.db import models

class SellerModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = PhoneNumberField(unique=True)
    store_name = models.CharField(max_length=255)
    gstin_number = models.CharField(max_length=15, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_name} ({self.user.email})"

class CategoryModel(models.Model):
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('seller', 'name')

    def __str__(self):
        return f"{self.name} - {self.seller.store_name}"

class SubCategoryModel(models.Model):
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='sub_categories_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('seller', 'name', 'category')

    def __str__(self):
        return f"{self.name} -> {self.category.name} ({self.seller.store_name})"