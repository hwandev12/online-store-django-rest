from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

class DeveloperHomePage(TemplateView):
    template_name = 'developer'

