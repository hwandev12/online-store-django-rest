from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", views.ProductListApiView, basename="product")
router.register(r"users", views.UserApiView, basename='user'),
router.register(r"sellers", views.SellerUserApiView, basename='seller'),
router.register(r"buyers", views.BuyerUserApiView, basename='buyer'),
router.register(r"product-image", views.ProductImageApiView, basename='product-image'),
router.register(r"product-category", views.ProductCategoryApiView, basename="product-category")
router.register(r"product-comment", views.CommentApiView, basename="product-comment")

urlpatterns = [
    path("", include(router.urls))
]