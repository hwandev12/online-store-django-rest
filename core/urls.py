from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.base.urls")),
    path('authentication/', include('allauth.urls')),
    path("", include("apps.authentication.urls")),
    path("developer/", include("apps.developer.urls")),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
