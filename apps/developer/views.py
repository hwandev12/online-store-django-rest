from typing import Optional
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.product.models import Product, Checkout

from django.contrib.auth.mixins import UserPassesTestMixin

from datetime import datetime, timedelta

class DeveloperHomePage(UserPassesTestMixin ,ListView):
    template_name = 'developer/pages/develop.html'
    context_object_name = 'apps'
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(DeveloperHomePage, self).get_queryset(*args, **kwargs)
        return qs
    
    def get_context_data(self, *args, **kwargs):
        context = super(DeveloperHomePage, self).get_context_data(*args, **kwargs)
        context['recent_sales'] = Checkout.objects.filter(ordered_date__gte=datetime.now()-timedelta(days=5)).order_by('-ordered_date')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeveloperHomePage, self).dispatch(*args, **kwargs)
    
    def test_func(self):
        if self.request.user.is_developer:
            return True
        return False


developer_home_page = DeveloperHomePage.as_view()