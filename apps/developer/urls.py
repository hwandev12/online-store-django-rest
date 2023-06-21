from django.urls import path
from .views import (
    developer_home_page
)

app_name = 'developer'

urlpatterns = [
    path('', developer_home_page, name='home'),
]