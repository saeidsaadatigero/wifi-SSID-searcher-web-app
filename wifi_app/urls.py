from django.urls import path
from .views import home, connect

urlpatterns = [
    path('', home, name='home'),
    path('connect/<str:wifi_name>/', connect, name='connect'),
]
