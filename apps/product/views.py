from django.shortcuts import render
# import Product from models.py, write a class to get all products
from .models import(
    Product,
    ProductCategory
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
        # get product by slug
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        return context
    
    

product_view = ProductView.as_view()
checkout_page_view = CheckoutPageView.as_view()