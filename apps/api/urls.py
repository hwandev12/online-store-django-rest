from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", views.ProductListApiView, basename="product")
router.register(r"users", views.UserApiView, basename='user'),
router.register(r"sellers", views.SellerUserApiView, basename='seller'),
router.register(r"seller-profile", views.SellerProfileApiView, basename="seller-profile")
router.register(r"buyer-profile", views.BuyerProfileApiView, basename="buyer-profile")
router.register(r"buyers", views.BuyerUserApiView, basename='buyer'),
# for product section
router.register(r"product-image", views.ProductImageApiView, basename='product-image'),
router.register(r"product-category", views.ProductCategoryApiView, basename="product-category")
router.register(r"product-comment", views.CommentApiView, basename="product-comment")
router.register(r"rating-product", views.RatingProductApiView, basename="product-rating")
router.register(r"product-cart", views.CheckoutItemApiView, basename="product-cart")
router.register(r"product-order", views.OrderApiView, basename="product-order")

urlpatterns = [
    path("", include(router.urls))
]