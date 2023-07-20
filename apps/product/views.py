from django.shortcuts import render, redirect, get_object_or_404
# import Product from models.py, write a class to get all products
from .models import(
    Product,
    ProductCategory,
    Checkout,
    Comment,
    RatingProduct,
    CheckoutItem
)
from django.views.generic import(
    ListView,
    DetailView
)
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# import method decorator
from django.utils.decorators import method_decorator
from .forms import (
    CheckoutForm,
)

import django_filters

# filter products
class ProductFilter(django_filters.FilterSet):
    product_cost = django_filters.NumberFilter()
    product_cost__gt = django_filters.NumberFilter(field_name='product_cost', lookup_expr='gt')
    product_cost__lt = django_filters.NumberFilter(field_name='product_cost', lookup_expr='lt')
    class Meta:
        model = Product
        fields = ['product_name', 'product_cost']

# ----------------- Products ----------------- #
class ProductView(ListView):
    model = Product
    template_name = 'pages/all_products.html'
    context_object_name = 'products'

    # write a method to get products by category
    def get_products_by_category(self):
        # write a code to paginate products
        product_filter = ProductFilter(self.request.GET, queryset=self.get_queryset())
        paginate = Paginator(product_filter.qs, 3)
        page_number = self.request.GET.get('page')
        product_page_obj = paginate.get_page(page_number)
        category = self.request.GET.get('product-category', None)
        if category:
            products = Product.objects.filter(category__category_name=category)
            paginate = Paginator(products, 3)
            page_number = self.request.GET.get('page')
            product_page_obj = paginate.get_page(page_number)
        else:
            product_page_obj = paginate.get_page(page_number)
        return product_page_obj    

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['product_categories'] = ProductCategory.objects.all()
        # write a method to get products by category
        context['product_page_obj'] = self.get_products_by_category()
        context["product_filter"] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        
        return context
# ----------------- Products ----------------- #

# ----------------- Checkouts ----------------- #
class CheckoutPageView(DetailView):
    model = Product
    template_name = 'pages/checkout.html'
    context_object_name = 'product'
    
    # write a method decorator
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.is_buyer:
            return super(CheckoutPageView, self).dispatch(request, *args, **kwargs)
        else:
            return render(request, 'pages/404.html',status=404)
    
    def get_context_data(self, **kwargs):
        context = super(CheckoutPageView, self).get_context_data(**kwargs)
        if not self.request.user.is_seller:
            context['form'] = CheckoutForm()
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        return context
    
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_seller and self.request.user.is_authenticated:
            if self.request.method == "POST":
                form = CheckoutForm(self.request.POST)
                if form.is_valid():
                    firstname = form.cleaned_data.get('firstname')
                    lastname = form.cleaned_data.get('lastname')
                    phone_number = form.cleaned_data.get('phone_number')
                    post_office = form.cleaned_data.get('post_office')
                    email = form.cleaned_data.get('email')
                    address = form.cleaned_data.get('address')
                    city = form.cleaned_data.get('city')
                    house = form.cleaned_data.get('house')
                    postal_code = form.cleaned_data.get('postal_code')
                    message = form.cleaned_data.get('message')
                new_checkout = Checkout(firstname=firstname, lastname=lastname, phone_number=phone_number, post_office=post_office, email=email, address=address, city=city, house=house, postal_code=postal_code, message=message, user=self.request.user.buyeraccountmodel, ordered=True, product=self.get_object())
                new_checkout.save()
                return redirect('base:product_detail', slug=self.get_object().slug)
        else:
            pass
# ----------------- Checkouts ----------------- #    
    
# ----------------- Add to cart ----------------- #
@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    try:
        checkout_item = CheckoutItem.objects.get(user=request.user, product=product, ordered=False)
    except:
        checkout_item = []
    if checkout_item:
        messages.info(request, "You already have this product on your cart", extra_tags="already_have")
        return redirect('base:product_detail', slug=slug)
    else:
        CheckoutItem.objects.create(user=request.user, product=product, ordered=False)
        messages.info(request, "This item was added to your cart.", extra_tags='add_cart')
    return redirect('base:product_detail', slug=slug)
# ----------------- Add to cart ----------------- #

# ----------------- Remove from cart ----------------- #
@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    checkout_qs = CheckoutItem.objects.filter(product=product, user=request.user, ordered=False)
    if checkout_qs:
        checkout_qs.delete()
        messages.info(request, "This item was removed from your cart.", extra_tags='remove_cart')
        return redirect('base:product_detail', slug=slug)
    else:
        messages.info(request, "This item was not in your cart.", extra_tags='not_in_cart')
        return redirect('base:product_detail', slug=slug)
# ----------------- Remove from cart ----------------- #

# ----------------- Remove single item from cart ----------------- #
@login_required
def remove_single_item_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    checkout_qs = Checkout.objects.filter(user=request.user, ordered=False)
    if checkout_qs.exists():
        checkout = checkout_qs[0]
        if checkout.checkout_items.filter(product__slug=product.slug).exists():
            checkout_item = CheckoutItem.objects.filter(product=product, user=request.user, ordered=False)[0]
            if checkout_item.quantity > 1:
                checkout_item.quantity -= 1
                checkout_item.save()
            else:
                checkout.checkout_items.remove(checkout_item)
            messages.info(request, "This item quantity was updated.", extra_tags='remove_single_cart')
            return redirect('base:product_detail', slug=slug)
        else:
            messages.info(request, "This item was not in your cart.", extra_tags='remove_single_cart')
            return redirect('base:product_detail', slug=slug)
    else:
        messages.info(request, "You do not have an active order.", extra_tags='remove_single_cart')
        return redirect('base:product_detail', slug=slug)
# ----------------- Remove single item from cart ----------------- #

# ----------------- cart section ----------------- #
class ProductCart(ListView):
    model = CheckoutItem
    template_name = 'pages/cart.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.buyeraccountmodel:
            return super(ProductCart, self).dispatch(request, *args, **kwargs)
        else:
            # later change to 404
            return redirect('base:home')
    
    def get_queryset(self):
        return CheckoutItem.objects.filter(user=self.request.user.buyeraccountmodel, ordered=False)
    
    def get_context_data(self, **kwargs):
        context = super(ProductCart, self).get_context_data(**kwargs)
        context['carts'] = self.get_queryset()
        # get total carts
        context['total_carts'] = self.get_queryset().count()
        return context
# ----------------- cart section ----------------- #

# ----------------- My Orders ----------------- #
class MyOrdersView(ListView):
    model = Checkout
    template_name = 'components/orders.html'
    context_object_name = 'orders'
    
    def get_queryset(self):
        return Checkout.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(MyOrdersView, self).get_context_data(**kwargs)
        context['orders'] = self.get_queryset()
        return context
# ----------------- My Orders ----------------- #

# ----------------- My Comments ----------------- #
class CommentForEachUserView(ListView):
    model = Comment
    template_name = 'components/comment.html'
    context_object_name = 'comments'
    
    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(CommentForEachUserView, self).get_context_data(**kwargs)
        context['comments'] = self.get_queryset()
        # get rating for each product and user
        context['rating'] = RatingProduct.objects.filter(user=self.request.user)
        return context
# ----------------- My Comments ----------------- #

product_view = ProductView.as_view()
checkout_page_view = CheckoutPageView.as_view()
my_orders_view = MyOrdersView.as_view()
my_comments_view = CommentForEachUserView.as_view()
product_cart_view = ProductCart.as_view()