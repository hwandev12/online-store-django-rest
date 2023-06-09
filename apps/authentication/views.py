from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from django.views import generic
from .forms import (
    StoreSellerAccountForm,
    CustomSellerAccountFormDjango,
    CustomBuyerAccountFormDjango,
    UpdateBuyerAccount,
    UpdateUserForm,
    UpdateSellerAccount
)

from django.contrib.auth import login

from .models import (
    User,
    BuyerAccountModel
)

class SellerRegisterView(generic.CreateView):
    model = User
    form_class = CustomSellerAccountFormDjango
    template_name = 'account/seller_register.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super(SellerRegisterView, self).get(request, *args, **kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')
    

class BuyerRegisterView(generic.CreateView):
    model = User
    form_class = CustomBuyerAccountFormDjango
    template_name = 'account/signup.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super(BuyerRegisterView, self).get(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')    

def user_profile(request, pk):
    request_get_pk = User.objects.get(id=pk)
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if not request.user.is_seller:
            account_model_update = UpdateBuyerAccount(request.POST, instance=request.user.buyeraccountmodel)
        else:
            account_model_update = UpdateSellerAccount(request.POST, instance=request.user.selleraccountmodel)
        
        if user_form.is_valid():
            user_form.save()
            account_model_update.save()
            return redirect("/")
    else:
        user_form = UpdateUserForm(instance=request.user)
        if not request.user.is_seller:
            account_model_update = UpdateBuyerAccount(instance=request.user.buyeraccountmodel)
        else:
            account_model_update = UpdateSellerAccount(instance=request.user.selleraccountmodel)    
        
    context = {
        "user_form": user_form,
        "account_model_update": account_model_update,
        "request_get_pk": request_get_pk
    }
    
    return render(request, 'account/profile.html', context)
    
seller_register = SellerRegisterView.as_view()
buyer_register = BuyerRegisterView.as_view()
# user_profile = UserProfileView.as_view()
