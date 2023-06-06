from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.authentication.views import (
    seller_register, 
    user_profile,
    buyer_register
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.base.urls")),
    path('authentication/', include('allauth.urls')),
    path("authentication/seller-register/", seller_register),
    path("authentication/signups/", buyer_register),
    path('authentication/profile/', user_profile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
