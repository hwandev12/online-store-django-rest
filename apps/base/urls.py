from django.urls import path
from .views import (
    home_page_view,
    welcome_page,
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_update_view,
    delete_comment,
)

from apps.product.views import (
    product_view,
    checkout_page_view,
    my_orders_view,
    my_comments_view
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
    path('product/update/<slug:slug>/', product_update_view, name='product_update'),
    
    # specific path for products
    path("products/", product_view, name='products'),
    path("product/comment/delete/<slug:slug>/<int:comment_id>/", delete_comment, name='delete_comment'),   
    
    # checkout pages
    path("product/single/checkout/<slug:slug>/", checkout_page_view, name='checkout')
]