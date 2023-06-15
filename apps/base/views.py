from typing import Any
from django import http
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView

from apps.product.models import Product

class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # create a method to get all products
    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        # filter products by date
        context['latest_products'] = Product.objects.all().order_by('-created_at')[:3]
        return context
       
class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    context_object_name = 'product'
    
class WelcomePage(TemplateView):
    template_name = 'components/welcome_choose.html'
    
# make classes to functionable
home_page_view = HomePageView.as_view()
welcome_page = WelcomePage.as_view()
# create a function name from class
product_detail_view = ProductDetailView.as_view()