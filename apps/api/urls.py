from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.api_root),
    path('products/', views.product_lists, name='products-api'),
    path('products/<int:pk>/', views.product_detail, name='product-detail-api'),
    # -- for seller user -- #
    path('seller-users/', views.seller_user_lists, name='seller-users-api'),
    path('seller-users/<int:pk>/', views.seller_user_detail, name='seller-user-detail-api'),
    # -- for buyer user -- #
    path('buyer-users/', views.buyer_user_lists, name='buyer-users-api'),
    path('buyer-users/<int:pk>/', views.buyer_user_detail, name='buyer-user-detail-api'),
    # -- for users -- #
    path('users/', views.user_lists, name='user-lists'),
    path('users/<int:pk>', views.user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)