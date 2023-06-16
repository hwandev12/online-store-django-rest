from django.urls import path
from .views import (
    home_page_view,
    welcome_page,
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_update_view
)

app_name = 'base'

urlpatterns = [
    path("", home_page_view, name='home'),
    path("welcome/", welcome_page, name='welcome'),
    # create a path for product detail
    path("product/single/<slug:slug>/", product_detail_view, name='product_detail'),
    # create a path for product create
    path("product/create/", product_create_view, name='product_create'),
    path("product/delete/<slug:slug>/", product_delete_view, name='product_delete'),
    path('product/update/<slug:slug>/', product_update_view, name='product_update')
]