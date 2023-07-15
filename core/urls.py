from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.base.urls")),
    path('authentication/', include('allauth.urls')),
    re_path(r"^inboxes/notify/", include("notifications.urls", namespace="notifications")),
    path("", include("apps.authentication.urls")),
    path("developer/", include("apps.developer.urls")),
    path("chat/", include("apps.chat.urls")),
    path('api/v1/', include("apps.api.urls")),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path("__debug__/", include("debug_toolbar.urls")),
    # re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# by this way we can append django_unicorn urls to urlpatterns
urlpatterns.append(path("unicorn/", include("django_unicorn.urls")),)


handler404 = "apps.base.views.not_found_404"
handler403 = "apps.base.views.page_not_permission"