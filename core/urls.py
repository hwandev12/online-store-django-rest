from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.authentication.views import seller_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.base.urls")),
    path('authentication/', include('allauth.urls')),
    path("seller-register/", seller_register),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
