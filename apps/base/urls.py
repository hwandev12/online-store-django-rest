from django.urls import path
from .views import (
    home_page_view,
    welcome_page,
    product_detail_view
)

app_name = 'base'

urlpatterns = [
    path("", home_page_view, name='home'),
    path("welcome/", welcome_page, name='welcome'),
    # create a path for product detail
    path("product/<slug:slug>/", product_detail_view, name='product_detail'),
]