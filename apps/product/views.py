from django.shortcuts import render, redirect
# import Product from models.py, write a class to get all products
from .models import(
    Product,
    ProductCategory,
    Checkout,
    Comment,
    RatingProduct
)
from django.views.generic import(
    ListView,
    DetailView
)
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required
# import method decorator
from django.utils.decorators import method_decorator
from .forms import (
    CheckoutForm,
)


class ProductView(ListView):
    model = Product
    template_name = 'pages/all_products.html'
    context_object_name = 'products'

    # write a method to get products by category
    def get_products_by_category(self):
        # write a code to paginate products
        paginate = Paginator(self.get_queryset(), 3)
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
        return context


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
                new_checkout = Checkout(firstname=firstname, lastname=lastname, phone_number=phone_number, post_office=post_office, email=email, address=address, city=city, house=house, postal_code=postal_code, message=message, user=self.request.user, product=self.get_object())
                new_checkout.save()
                return redirect('base:product_detail', slug=self.get_object().slug)
        else:
            pass
    
    
# create myOrders class
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


product_view = ProductView.as_view()
checkout_page_view = CheckoutPageView.as_view()
my_orders_view = MyOrdersView.as_view()
my_comments_view = CommentForEachUserView.as_view()