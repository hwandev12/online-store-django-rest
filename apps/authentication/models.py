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
    
    def create_user(self, email, username, phone_number, password=None):
        if not username:
            raise ValueError("User must have username")
        if not email:
            raise ValueError("User must have password")
        
        user = self.model(email=self.normalize_email(email), username=username,phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_number, password=None):
        if password is None:
            raise TypeError("You should write password fields!")
        
        user = self.create_user(email, username, phone_number, password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
        
    username = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    phone_number = models.IntegerField(default=998)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    def token(self):
        return ""
    

@receiver(user_signed_up)
def user_signup_callback(sender, user, request, **kwargs):
    messages.success(request, "", extra_tags="signup")