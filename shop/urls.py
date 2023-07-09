from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('carshop', views.carshop, name='carshop'),
    path('engines', views.engines, name='engines'),
    path('car_list', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('manufacturercountry', views.manufacturercountry, name='manufacturercountry'),
]
