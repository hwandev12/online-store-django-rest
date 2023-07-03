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
    my_comments_view,
    add_to_cart,
    product_cart_view,
    remove_from_cart,
    remove_single_item_from_cart,
)

app_name = 'base'

urlpatterns = [
    path("", home_page_view, name='home'),
    path("welcome/", welcome_page, name='welcome'),
    # create a path for product detail
    path("product/single/user/<slug:slug>/", product_detail_view, name='product_detail'),
    # create a path for product create
    path("product/create/", product_create_view, name='product_create'),
    path("product/delete/<slug:slug>/", product_delete_view, name='product_delete'),
    path('product/update/<slug:slug>/', product_update_view, name='product_update'),
    
    # specific path for products
    path("products/", product_view, name='products'),
    path("product/comment/delete/<slug:slug>/<int:comment_id>/", delete_comment, name='delete_comment'),   
    
    # checkout pages
    path("product/single/checkout/<slug:slug>/", checkout_page_view, name='checkout'),
    path("product/single/checkout/add/<slug:slug>/", add_to_cart, name='add_to_cart'),
    path("product/single/cart/", product_cart_view, name='cart'),
    path("product/remove-from-cart/<slug>/", remove_from_cart, name='remove_from_cart'),
    path("product/single/cart/remove/single/<slug>/", remove_single_item_from_cart, name='remove_single_item_from_cart'),
]