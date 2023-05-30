from django.urls import path
from .views import (
    home_page_view
)

app_name = 'base'

urlpatterns = [
    path("", home_page_view, name='home')
]