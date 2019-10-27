from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('one/', views.stock_get, name='getstock'),
    path('final/', views.stock_display, name='stockdisplay'),
]
