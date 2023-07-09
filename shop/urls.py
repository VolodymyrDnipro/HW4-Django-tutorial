from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('carshop', views.carshop, name='carshop'),
    path('engines', views.engines, name='engines'),
    path('cars', views.cars, name='cars'),
    path('car/<int:car_id>/', views.car_detail, name='car-detail'),
    path('manufacturercountry', views.manufacturercountry, name='manufacturercountry'),
]
