from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage, name='manage'),
    path('foods/', views.foods, name='foods'),
    path('orders/', views.orders, name='orders'),
]