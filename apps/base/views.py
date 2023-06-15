from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse
from apps.product.models import Product
from apps.product.forms import ProductForm
class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # create a method to get all products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['latest_products'] = Product.objects.all().order_by('-created_at')[:3]
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    context_object_name = 'product'
    
    
# create product create class
class ProductCreateView(CreateView):
    template_name = 'pages/product_create.html'
    form_class = ProductForm
    
    # create method to allow only seller to create product
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_seller:
            # later on i would add 404 page here
            return redirect('base:home')
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.owner = self.request.user.selleraccountmodel
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('base:product_detail', args=[self.object.slug])
    
    
class WelcomePage(TemplateView):
    template_name = 'components/welcome_choose.html'
    
    
# create not found page class view
# class NotFound(TemplateView):
#     template_name = 'pages/not_found.html'
    
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

# make classes to functionable
home_page_view = HomePageView.as_view()
welcome_page = WelcomePage.as_view()
# create a function name from class
product_detail_view = ProductDetailView.as_view()
product_create_view = ProductCreateView.as_view()