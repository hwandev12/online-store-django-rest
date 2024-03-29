from django.urls import path, re_path
from .views import (
    seller_register,
    buyer_register,
    user_profile,
    profile,
    add_follower,
    remove_follower,
)


from apps.notification.views import (
    mark_as_read,
    single_notification,
    all_notifications,
    unread_notifications,
    sent_mail,
    mark_all_as_read,
)

app_name = "authentication"

urlpatterns = [
    path("authentication/seller-register/", seller_register, name="seller_register"),
    path("authentication/register/", buyer_register, name="buyer_register"),
    path('authentication/profile/<str:firstname>/edit/', user_profile, name="profile-edit"),
    path("profile/<str:first_name>/", profile, name="general_profile"),
    # notification paths
    re_path(r'^inbox/notify/mark-as-read/(?P<slug>\d+)/$', mark_as_read, name='mark_as_read'),
    path('inbox/notify/mark-all-as-read/', mark_all_as_read, name='mark_all_as_read'),
    path('inbox/notify/<int:pk>/', single_notification, name='single_notification'),
    path('inbox/notifications/', all_notifications, name='all_notifications'),
    path('inbox/notifications/unread/', unread_notifications, name='unread_notifications'),
    path('inbox/notifications/sent-mail/', sent_mail, name='sent_mail'),
    path('profile-following/<str:first_name>/<slug:slug>/', add_follower, name="add_follower"),
    path('profile-unfollowing/<str:first_name>/<slug:slug>/', remove_follower, name="remove_follower")
]