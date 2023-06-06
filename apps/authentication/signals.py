from django.db.models.signals import post_save
from .models import User, BuyerProfile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_buyer_profile(sender, instance, created, **kwargs):
    if created:
        BuyerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_buyer_profile(sender, instance, **kwargs):
    instance.buyerprofile.save()