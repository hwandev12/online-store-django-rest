from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from .forms import (
    UserCreationForm,
    UserUpdateForm
)

from django.contrib.auth.decorators import login_required

class CustomUserAdmin(admin.ModelAdmin):
    
    form = UserUpdateForm
    add_form = UserCreationForm
    
    list_display = ["email", "username", "phone_number", "is_superuser"]
    list_filter = ["is_superuser"]
    search_fields = ["email"]
    ordering = ["email"]


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.login = login_required(admin.site.login)

