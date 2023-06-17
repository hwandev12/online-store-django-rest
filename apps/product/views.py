from django.shortcuts import render
# import Product from models.py, write a class to get all products
from .models import Product
from django.views.generic import ListView, DetailView

class ProductView(ListView):
    model = Product
    template_name = 'pages/all_products.html'
    context_object_name = 'products'
    

product_view = ProductView.as_view()
