from django.shortcuts import render
from allauth.account.views import SignupView

from .forms import StoreSellerAccountForm

class SellerRegisterView(SignupView):
    
    template_name = 'account/seller_register.html'
    form_class = StoreSellerAccountForm
    redirect_field_name = 'next'
    view_name = "seller_register"
    
    def get_context_data(self, **kwargs):
        user = super(SellerRegisterView, self).get_context_data(**kwargs)
        user.update(**kwargs)
        return user
    
seller_register = SellerRegisterView.as_view()
