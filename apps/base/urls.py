from django.urls import path
from .views import (
    home_page_view,
    welcome_page
)

app_name = 'base'

urlpatterns = [
    path("", home_page_view, name='home'),
    path("welcome/", welcome_page, name='welcome')
]