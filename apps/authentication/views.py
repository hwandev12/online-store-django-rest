from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.views import SignupView
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import (
    StoreSellerAccountForm,
    CustomSellerAccountFormDjango,
    CustomBuyerAccountFormDjango,
    UpdateBuyerAccount,
    UpdateUserForm,
    UpdateSellerAccount,
    UpdateBuyerProfile,
    UpdateSellerProfile
)
from django.contrib import messages

from django.contrib.auth import login

from datetime import datetime

from .models import (
    User,
    BuyerAccountModel,
    SellerAccountModel,
    SellerProfile,
)
from apps.product.models import (
    Product,
    Comment,
    RatingProduct,
    Checkout
)
from notifications.models import Notification
from notifications.templatetags.notifications_tags import live_notify_list, register_notify_callbacks

# ------------------- Seller Register ------------------- #
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
# ------------------- Seller Register ------------------- #

# ------------------- Buyer Register ------------------- #
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
# ------------------- Buyer Register ------------------- #

# ------------------- Update Profile ------------------- #
def user_profile(request, firstname):
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if request.user.is_buyer:
            account_model_update = UpdateBuyerAccount(request.POST, instance=request.user.buyeraccountmodel)
            account_profile_update = UpdateBuyerProfile(request.POST, request.FILES, instance=request.user.buyeraccountmodel.buyerprofile)
        elif request.user.is_seller:
            account_model_update = UpdateSellerAccount(request.POST, instance=request.user.selleraccountmodel)
            account_profile_update = UpdateSellerProfile(request.POST, request.FILES, instance=request.user.selleraccountmodel.sellerprofile)
        # this is for superuser accounts
        else:
            account_model_update = User(request.POST, instance=request.user)
        
        if user_form.is_valid():
            user_form.save()
            account_model_update.save()
            account_profile_update.save()
            messages.success(request, "Your profile is updated successfully", extra_tags="profile_update")
            return redirect("/")
    else:
        user_form = UpdateUserForm(instance=request.user)
        if request.user.is_buyer:
            account_model_update = UpdateBuyerAccount(instance=request.user.buyeraccountmodel)
            account_profile_update = UpdateBuyerProfile(instance=request.user.buyeraccountmodel.buyer_profile)
        elif request.user.is_seller:
            account_model_update = UpdateSellerAccount(instance=request.user.selleraccountmodel)  
            account_profile_update = UpdateSellerProfile(instance=request.user.selleraccountmodel.seller_profile)  
        else:
            account_model_update = UpdateUserForm(instance=request.user)
            account_profile_update = None
        
    context = {
        "user_form": user_form,
        "account_model_update": account_model_update,
        "account_profile_update": account_profile_update
    }
    
    return render(request, 'account/profile-update.html', context)
# ------------------- Update Profile ------------------- #

# ------------------- User Profile ------------------- #
@login_required()
def profile(request, first_name):
    seller = None
    seller_profile = None
    not_owned_profile = None
    buyer = None
    user = None
    product = None
    orders = None
    comments = None
    notice = None
    followers = None
    is_following = False
    count_of_followers = 0
    product_count = 0
    if request.user.is_seller:
        try:
            seller = get_object_or_404(SellerAccountModel, user=request.user, first_name=first_name)
            seller_profile = get_object_or_404(SellerProfile, user=seller)
            notice = Notification.objects.filter(recipient=request.user)
            product = Product.objects.filter(owner=request.user.selleraccountmodel)
            product_count = product.count()
            followers = seller_profile.followers.all()
            if len(followers) == 0:
                is_following = False
            
            for follower in followers:
                if follower == request.user:
                    is_following = True
                    break
                else:
                    is_following = False    
                    
            count_of_followers = len(followers)
            
        except ValueError as e:
            # we should change this 404 error page later on
            return redirect("/")
    elif request.user.is_buyer:
        try:
            try:
                buyer = get_object_or_404(BuyerAccountModel, user=request.user, first_name=first_name)
            except:
                not_owned_profile = get_object_or_404(SellerAccountModel, first_name=first_name)
            try:
                not_owned_profile = get_object_or_404(SellerAccountModel, first_name=first_name)
            except:
                buyer = get_object_or_404(BuyerAccountModel, user=request.user, first_name=first_name)
            orders = Checkout.objects.filter(user=request.user.buyeraccountmodel)
            comments = Comment.objects.filter(user=request.user)
        except ValueError as e:
            print("Hatoo")
            # we should change this 404 error page later on
            return redirect("/")
    else:
        try:
            user = get_object_or_404(User, id=first_name, email=request.user.email)
            notice = user.notifications.unread()
        except ValueError as e:
            # we should change this 404 error page later on
            return redirect("/")
    
    
    # get latest product
    if product:
        product = product.order_by('-created_at')[:3]
    else:
        product = None
        
    context = {
        "seller": seller,
        "buyer": buyer,
        "user": user,
        "product": product,
        "orders": orders,
        "comments": comments,
        "notice": notice,
        "followers": followers,
        "is_following": is_following,
        "count_of_followers": count_of_followers,
        "product_count": product_count,
        "not_owned_profile": not_owned_profile
    }
    return render(request, 'account/profile.html', context)
# ------------------- User Profile ------------------- #
    
# ------------------- Follow User ------------------- #
class AddFollowersForSellerAccountModel(LoginRequiredMixin, UserPassesTestMixin, View):
    
    def post(self, request, first_name, slug, *args, **kwargs):
        seller = get_object_or_404(SellerAccountModel, first_name=first_name)
        profile = get_object_or_404(SellerProfile, user=seller)
        product = Product.objects.get(slug=slug)
        profile.followers.add(request.user)
        
        return redirect("base:product_detail", slug=product.slug)
    
    def test_func(self):
        if self.request.user.is_buyer:
            return True
        return False
    
# ------------------- Follow User ------------------- #

# ------------------- Unfollow User ------------------- #
class RemoveFollowersForSellerAccountModel(LoginRequiredMixin, UserPassesTestMixin, View):

    def post(self, request, first_name, slug, *args, **kwargs):
        seller = get_object_or_404(SellerAccountModel, first_name=first_name)
        profile = get_object_or_404(SellerProfile, user=seller)
        product = Product.objects.get(slug=slug)
        profile.followers.remove(request.user)

        return redirect("base:product_detail", slug=product.slug)
    
    def test_func(self):
        if self.request.user.is_buyer:
            return True
        return False
# ------------------- Unfollow User ------------------- #
    
seller_register = SellerRegisterView.as_view()
buyer_register = BuyerRegisterView.as_view()
add_follower = AddFollowersForSellerAccountModel.as_view()
remove_follower = RemoveFollowersForSellerAccountModel.as_view()