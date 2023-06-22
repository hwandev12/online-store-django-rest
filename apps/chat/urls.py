from django.urls import path
from .views import room

app_name = "chat"

urlpatterns = [
    path('<str:room_name>/', room, name='room')
]