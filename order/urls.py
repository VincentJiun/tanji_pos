from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('check/', views.check),

    re_path(r'q(?P<order_id>[\d]+)', views.QueryOrder),
]