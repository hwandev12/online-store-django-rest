from typing import Any
from django import http
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class WelcomePage(TemplateView):
    template_name = 'components/welcome_choose.html'
    
# make classes to functionable
home_page_view = HomePageView.as_view()
welcome_page = WelcomePage.as_view()
