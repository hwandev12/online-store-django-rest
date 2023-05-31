from django import forms
from .models import User
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