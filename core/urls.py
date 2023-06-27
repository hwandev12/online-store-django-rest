from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.base.urls")),
    path('authentication/', include('allauth.urls')),
    re_path(r"^inboxes/great/sk/", include("notifications.urls", namespace="notifications")),
    path("", include("apps.authentication.urls")),
    path("developer/", include("apps.developer.urls")),
    path("chat/", include("apps.chat.urls")),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    # re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
