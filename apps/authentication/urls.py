from django.urls import path
from .views import (
    seller_register,
    buyer_register,
    user_profile
)

app_name = "authentication"

urlpatterns = [
    path("authentication/seller-register/", seller_register, name="seller_register"),
    path("authentication/register/", buyer_register, name="buyer_register"),
    path('authentication/profile/<str:firstname>', user_profile, name="profile")
]