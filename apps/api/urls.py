from django.urls import path, include, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from allauth.account.views import ConfirmEmailView

router = DefaultRouter()
router.register(r"users", views.UserApiView, basename='user'),
router.register(r"sellers", views.SellerUserApiView, basename='seller'),
router.register(r"buyers", views.BuyerUserApiView, basename='buyer'),
# for product section
router.register(r"product-image", views.ProductImageApiView, basename='product-image'),
router.register(r"product-category", views.ProductCategoryApiView, basename="product-category")
router.register(r"product-comment", views.CommentApiView, basename="product-comment")
router.register(r"rating-product", views.RatingProductApiView, basename="product-rating")
router.register(r"product-cart", views.CheckoutItemApiView, basename="product-cart")
router.register(r"product-order", views.OrderApiView, basename="product-order")

urlpatterns = [
    path("", include(router.urls)),
    # for user authentication and authorization
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),
    name='account_confirm_email'),
    path('register/seller', views.SellerRegisterApiView.as_view()),
    path('register/buyer/', views.BuyerRegisterApiView.as_view()),
    
    # for product page
    path('products/', views.ProductListApiView.as_view(), name='api-product'),
    path('products/<slug:slug>/', views.ProductDetailApiView.as_view(), name='api-product-detail'),
    path('product/create/', views.ProductCreateApiView.as_view(), name='api-product-create'),
    path('product/update/<slug:slug>/', views.ProductUpdateApiView.as_view(), name="api-product-update"),
    path('product/delete/<slug:slug>/', views.ProductDeleteApiView.as_view(), name="api-product-delete")
]

