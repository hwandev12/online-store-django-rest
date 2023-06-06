from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

from django.contrib import messages
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have password")
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError("You should write password fields!")
        
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
        
    email = models.EmailField(unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # 
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def token(self):
        return ""
    
# create seller account
class SellerAccountModel(models.Model):
    
    class Meta:
        verbose_name = "Seller Account"
        verbose_name_plural = "Seller Account"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=998)
    
    def __str__(self):
        return self.user.email
    
class BuyerAccountModel(models.Model):
    
    class Meta:
        verbose_name = "Buyer Account"
        verbose_name_plural = "Buyer Account"
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=998)
    company = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.email
    
class BuyerProfile(models.Model):
    class Meta:
        verbose_name = "Buyer Profile"
        verbose_name_plural = "Buyer Profile"
        
    user = models.OneToOneField(BuyerAccountModel, on_delete=models.CASCADE)
    avatar = models.ImageField(default='users/user.png', upload_to='buyers/')

    def __str__(self):
        return self.user.first_name
    
class SellerProfile(models.Model):
    
    class Meta:
        verbose_name = "Seller Profile"
        verbose_name_plural = "Seller Profile"
        
    user = models.OneToOneField(SellerAccountModel, on_delete=models.CASCADE)
    avatar = models.ImageField(default="users/user.png", upload_to='sellers/')
    
    def __str__(self):
        return self.user.first_name

# we can configure as what we want login, logout, signup
# this is second way of doing that
# first way is just change the template name and override to complete task
@receiver(user_signed_up)
def user_signup_callback(sender, user, request, **kwargs):
    messages.success(request, "", extra_tags="signup")