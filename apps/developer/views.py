from typing import Optional
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.product.models import Product

from django.contrib.auth.mixins import UserPassesTestMixin
class DeveloperHomePage(UserPassesTestMixin ,ListView):
    template_name = 'developer/pages/develop.html'
    context_object_name = 'apps'
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(DeveloperHomePage, self).get_queryset(*args, **kwargs)
        return qs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeveloperHomePage, self).dispatch(*args, **kwargs)
    
    def test_func(self):
        if self.request.user.is_developer:
            return True
        return False


developer_home_page = DeveloperHomePage.as_view()