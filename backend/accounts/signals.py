from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUserModel
from customer.models import CustomerModel
from seller.models import SellerModel

@receiver(post_save, sender=CustomUserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.user_type == 'customer':
        CustomerModel.objects.get_or_create(user=instance)

    elif instance.user_type == 'seller':
        SellerModel.objects.get_or_create(user=instance)