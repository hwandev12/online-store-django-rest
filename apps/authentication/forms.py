from django import forms
from .models import (
    User,
    SellerAccountModel,
    BuyerAccountModel,
    BuyerProfile,
    SellerProfile
)
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction

from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm

# create a custom social signup form
class CustomSocialSignupForm(SocialSignupForm):
    first_name = forms.CharField(required=True, strip=True)
    last_name = forms.CharField(required=True, strip=True)
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    company = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Company")
    
    def save(self, request):
        user =  super(CustomSocialSignupForm, self).save(request)
        user.is_buyer = True
        user.save()
        buyer_account = BuyerAccountModel(
            user=user,
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            phone_number=self.cleaned_data.get("phone_number"),
            company=self.cleaned_data.get("company")
        )
        buyer_account.save()
        return buyer_account
class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}), label="")
    
    # username
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),label="")
    
    class Meta:
        model = User
        fields = ["email"]
        
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
    
    
class CustomSellerAccountFormDjango(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Phone Number"}), label="")
    organization = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_seller = True
        user.save()
        seller = SellerAccountModel.objects.create(user=user)
        seller.first_name = self.cleaned_data['first_name']
        seller.last_name = self.cleaned_data['last_name']
        seller.phone_number = self.cleaned_data['phone_number']
        seller.organization = self.cleaned_data['organization']
        seller.save()
        return user
    
class UserUpdateForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ["email",  "password", "is_superuser", "is_staff", "is_active", "is_verified"]
        

class CustomBuyerAccountFormDjango(UserCreationForm):
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Phone Number"}), label="")
    first_name = forms.CharField()
    last_name = forms.CharField()
    company = forms.CharField()
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_buyer = True
        user.save()
        buyer = BuyerAccountModel.objects.create(user=user)
        buyer.first_name = self.cleaned_data['first_name']
        buyer.last_name = self.cleaned_data['last_name']
        buyer.phone_number = self.cleaned_data['phone_number']
        buyer.company = self.cleaned_data['company']
        buyer.save()
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

# for updating uniuq user values, email, username, etc
class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["email",]
        
class UpdateBuyerAccount(forms.ModelForm):
    
    class Meta:
        model = BuyerAccountModel
        fields = ["first_name", "last_name", "phone_number", "company"]
        
class UpdateSellerAccount(forms.ModelForm):
    
    class Meta:
        model = SellerAccountModel
        fields = ['first_name', 'last_name', 'phone_number', 'organization']
        
class UpdateSellerProfile(forms.ModelForm):
    
    class Meta:
        model = SellerProfile
        fields = ["avatar"]
        
class UpdateBuyerProfile(forms.ModelForm):
    
    class Meta:
        model = BuyerProfile
        fields = ["avatar"]