from django.contrib import admin
from .models import (
    User,
    SellerAccountModel,
    BuyerProfile
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
    
    list_display = ["email", "username", "phone_number", "is_superuser", ]
    list_filter = ["is_superuser"]
    fields = ['email', 'username', 'phone_number', "is_superuser", 'is_active', 'is_staff', 'is_buyer', 'is_seller']
    search_fields = ["email"]
    ordering = ["email"]


class CustomSellerAccountAdmin(admin.ModelAdmin):
    
    list_display = ["first_name", "last_name" ,"username", "email"]
    
    def username(self, instance):
        try:
            return instance.user.username
        except ObjectDoesNotExist:
            return "Error"
    def email(self, instance):
        try:
            return instance.user.email
        except ObjectDoesNotExist:
            return "Error"

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(SellerAccountModel)
admin.site.register(BuyerProfile)
admin.site.login = login_required(admin.site.login)

