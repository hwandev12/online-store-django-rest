from django import forms
from .models import User, SellerAccountModel
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from allauth.account.forms import SignupForm


class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}), label="")
    
    # username
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}), label="")
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),label="")
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Phone Number"}), label="")
    
    class Meta:
        model = User
        fields = ["email", "username", "phone_number"]
        
    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match!")
        return password2
    
    def save(self, commit=True):
        
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserUpdateForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ["email", "username", "phone_number", "password", "is_superuser", "is_staff", "is_active", "is_verified"]
        

class CustomAllauthForm(SignupForm):
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Phone Number"}), label="")
    
    def save(self, request):
        user = super(CustomAllauthForm, self).save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
    
# By this we can create custom djagno allauth form with concise ways
# greate way!
# class SellerUserRegisterForm(SignupForm):
#     address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}), label="")
#     phone_number = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Phone Number"}), label="")
#     def save(self, request):
#         seller = super(SellerUserRegisterForm, self).save(request)
#         seller.address = self.cleaned_data["address"]
#         seller.phone_number = self.cleaned_data["phone_number"]
#         seller.is_seller = True
#         seller.save()
#         return seller
    
class StoreSellerAccountForm(SignupForm):
    
    first_name = forms.CharField(required=True, strip=True)
    last_name = forms.CharField(required=True, strip=True)
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    def save(self, request):
        user =  super(StoreSellerAccountForm, self).save(request)

        seller_account = SellerAccountModel(
            user=user,
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            phone_number=self.cleaned_data.get("phone_number"),
        )
        seller_account.save()
        return seller_account.user
