from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Online Storen Api",
        default_version="v1",
        description="Serving online store for consumers",
        terms_of_service="https://later-on-add-website.com/terms/",
        contact=openapi.Contact(email="contact@verification.local"),
        license=openapi.License(name="Verify License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

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
    re_path(r"^api/v2/", schema_view.with_ui("swagger", cache_timeout=0))
    # re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# by this way we can append django_unicorn urls to urlpatterns
urlpatterns.append(path("unicorn/", include("django_unicorn.urls")),)


handler404 = "apps.base.views.not_found_404"
handler403 = "apps.base.views.page_not_permission"