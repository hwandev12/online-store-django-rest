from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

from django.contrib import messages
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

# ------------------- Custom User Model ------------------- #
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
# ------------------- Custom User Model ------------------- #    

# ------------------- User Model ------------------- #
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

    # get buyera and seller profile avatar
    def get_buyer_avatar(self):
        return self.buyeraccountmodel.buyerprofile.avatar.url
# ------------------- User Model ------------------- #    

# ------------------- Seller Model ------------------- #
class SellerAccountModel(models.Model):
    
    class Meta:
        verbose_name = "Seller Account"
        verbose_name_plural = "Seller Account"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=998)
    organization = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.user.email
    
    # get seller profile avatar
    def get_seller_avatar(self):
        return self.sellerprofile.avatar.url
# ------------------- Seller Model ------------------- #

# ------------------- Buyer Model ------------------- #
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
    
    # get buyer profile avatar
    def get_buyer_avatar(self):
        return self.buyerprofile.avatar.url
    
# ------------------- Buyer Model ------------------- #

# ------------------- Buyer Profile ------------------- #
class BuyerProfile(models.Model):
    class Meta:
        verbose_name = "Buyer Profile"
        verbose_name_plural = "Buyer Profile"
        
    user = models.OneToOneField(BuyerAccountModel, on_delete=models.CASCADE)
    avatar = models.ImageField(default='users/user.png', upload_to='buyers/')

    def __str__(self):
        return self.user.first_name
# ------------------- Buyer Profile ------------------- #
    
# ------------------- Seller Profile ------------------- #
class SellerProfile(models.Model):
    
    class Meta:
        verbose_name = "Seller Profile"
        verbose_name_plural = "Seller Profile"
        
    user = models.OneToOneField(SellerAccountModel, on_delete=models.CASCADE)
    avatar = models.ImageField(default="users/user.png", upload_to='sellers/')
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    
    def __str__(self):
        return self.user.first_name
# ------------------- Seller Profile ------------------- #

@receiver(user_signed_up)
def user_signup_callback(sender, user, request, **kwargs):
    messages.success(request, "", extra_tags="signup")
