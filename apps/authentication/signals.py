from django.db.models.signals import post_save
from .models import (
    User,
    BuyerAccountModel,
    SellerAccountModel,
    BuyerProfile,
    SellerProfile
)
from django.dispatch import receiver

# for buyer profile
@receiver(post_save, sender=BuyerAccountModel)
def create_buyer_profile(sender, instance, created, **kwargs):
    if created:
        BuyerProfile.objects.create(user=instance)
    
    
# for seller profile 
@receiver(post_save, sender=SellerAccountModel)
def create_seller_profile(sender, instance, created, **kwargs):
    if created:
        SellerProfile.objects.create(user=instance)
    
