from django.shortcuts import render, get_object_or_404
from .models import Car


def index(request):
    return render(request, 'shop/index.html')


def carshop(request):
    return render(request, 'shop/carshop.html')


def engines(request):
    return render(request, 'shop/engines.html')


def cars(request):
    cars_list = Car.objects.all()
    context = {
        'cars_list': cars_list
    }
    return render(request, 'shop/cars.html', context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {
        'car': car
    }
    return render(request, 'shop/car_detail.html', context)

def manufacturercountry(request):
    return render(request, 'shop/manufacturercountry.html')
