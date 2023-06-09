from django.contrib import admin
from .models import (
    User,
    SellerAccountModel,
    BuyerProfile,
    BuyerAccountModel,
    SellerProfile,
)
from django.contrib.auth.models import Group
from .forms import (
    UserCreationForm,
    UserUpdateForm
)
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

class CustomUserAdmin(admin.ModelAdmin):
    
    form = UserUpdateForm
    add_form = UserCreationForm
    
    list_display = ["email", "is_superuser", "is_buyer", "is_seller"]
    list_filter = ["is_superuser"]
    fields = ['email', "is_superuser", 'is_active', 'is_staff', 'is_buyer', 'is_seller', "password"]
    search_fields = ["email"]
    ordering = ["email"]


class CustomSellerAccountAdmin(admin.ModelAdmin):
    
    list_display = ["first_name", "last_name" , "email"]
    
    def email(self, instance):
        try:
            return instance.user.email
        except ObjectDoesNotExist:
            return "Error"

admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(SellerAccountModel)
admin.site.register(BuyerProfile)
admin.site.register(BuyerAccountModel)
admin.site.register(SellerProfile)
admin.site.login = login_required(admin.site.login)

