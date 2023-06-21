from django.urls import path
from .views import (
    developer_home_page
)

urlpatterns = [
    path('', developer_home_page, name='home'),
]