from django.urls import path
from .views import (
    seller_register,
    buyer_register,
    user_profile,
    profile
)

app_name = "authentication"

urlpatterns = [
    path("authentication/seller-register/", seller_register, name="seller_register"),
    path("authentication/register/", buyer_register, name="buyer_register"),
    path('authentication/profile/<str:firstname>/edit/', user_profile, name="profile-edit"),
    path("profile/<str:first_name>/", profile, name="general_profile")
]