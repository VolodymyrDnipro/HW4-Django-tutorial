from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('carshop', views.carshop, name='carshop'),
    path('carshop/<int:carshop_id>/', views.carshop_detail, name='carshop_detail'),
    path('engine_list', views.engine_list, name='engine_list'),
    path('engine/<int:engine_id>/', views.engine_detail, name='engine_detail'),
    path('car_list', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('manufacturercountry_list', views.manufacturercountry_list, name='manufacturercountry_list'),
    path('manufacturercountry/<int:manufacturercountry_id>/', views.manufacturercountry_detail, name='manufacturercountry_detail'),
    path('color_list', views.color_list, name='color_list'),
    path('color/<int:color_id>/', views.color_detail, name='color_detail'),

]
