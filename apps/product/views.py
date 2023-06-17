from django.shortcuts import render
# import Product from models.py, write a class to get all products
from .models import Product, ProductCategory
from django.views.generic import ListView, DetailView
from django.db.models import Q


class ProductView(ListView):
    model = Product
    template_name = 'pages/all_products.html'
    context_object_name = 'products'

    # write a method to get products by category
    def get_products_by_category(self):
        category = self.request.GET.get('product-category', None)
        if category:
            products = Product.objects.filter(category__category_name=category)
        else:
            products = Product.objects.all()
        return products

    # get all productCategory

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['product_categories'] = ProductCategory.objects.all()
        # write a method to get products by category
        context['products_by_category'] = self.get_products_by_category()
        return context


product_view = ProductView.as_view()
