from django.urls import path
from .views import room, message_send_view

app_name = "chat"

urlpatterns = [
    path('group/<str:room_name>/', room, name='room'),
    path('send-message/<str:firstname>/', message_send_view, name='send-message')
]