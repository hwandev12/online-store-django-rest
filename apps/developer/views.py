from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.product.models import Product

class DeveloperHomePage(ListView):
    template_name = 'developer/pages/develop.html'
    context_object_name = 'apps'

    def get_queryset(self):
        return Product.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeveloperHomePage, self).dispatch(*args, **kwargs)


developer_home_page = DeveloperHomePage.as_view()   