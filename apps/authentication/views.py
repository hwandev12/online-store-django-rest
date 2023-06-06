from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from django.views import generic
from .forms import StoreSellerAccountForm, CustomSellerAccountFormDjango

from django.contrib.auth import login

from .models import User

class SellerRegisterView(generic.CreateView):
    model = User
    form_class = CustomSellerAccountFormDjango
    template_name = 'account/seller_register.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')
    
class UserProfileView(generic.TemplateView):
    template_name = 'account/profile.html'
    
seller_register = SellerRegisterView.as_view()
user_profile = UserProfileView.as_view()
