from django.shortcuts import render, get_object_or_404
from .models import Car, CarShop, Engine, ManufacturerCountry, Color
from django.core.paginator import Paginator
from django.db.models import Case, When, Value, CharField, Count, Sum

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.core.cache import cache

def index(request):
    return render(request, 'shop/index.html')


def carshop(request):
    shop_list = CarShop.objects.all()
    paginator = Paginator(shop_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'shop_list': page_obj
    }
    return render(request, 'shop/carshop.html', context=context)


def carshop_detail(request, carshop_id):
    carshop = get_object_or_404(CarShop, id=carshop_id)
    carshop_prefetched = CarShop.objects.select_related('car').annotate(
        total_count=Sum('count')
    ).get(id=carshop_id)

    context = {
        'carshop': carshop_prefetched
    }
    return render(request, 'shop/carshop_detail.html', context=context)


def engine_list(request):
    engine_list = Engine.objects.all()
    paginator = Paginator(engine_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'engine_list': page_obj
    }
    return render(request, 'shop/engine_list.html', context=context)


def engine_detail(request, engine_id):
    engine = get_object_or_404(Engine, id=engine_id)
    manufacturercountry = ManufacturerCountry.objects.filter(engine=engine).first()
    engine = engine.__class__.objects.annotate(
        power_range=Case(
            When(power__lte=100, then=Value('Low')),
            When(power__gt=100, power__lte=200, then=Value('Medium')),
            When(power__gt=200, then=Value('High')),
            default=Value('Unknown'),
            output_field=CharField(),
        )
    ).get(id=engine_id)
    context = {
        'engine': engine,
        'manufacturercountry': manufacturercountry
    }
    return render(request, 'shop/engine_detail.html', context=context)


def car_list(request):
    cars_list = Car.objects.all()
    paginator = Paginator(cars_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'cars_list': page_obj
    }
    return render(request, 'shop/car_list.html', context=context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car_prefetched = Car.objects.prefetch_related(
        'engine',
        'transmission',
        'color',
        'carshop_set'
    ).annotate(
        total_count=Count('carshop')
    ).get(id=car_id)

    context = {
        'car': car_prefetched
    }
    return render(request, 'shop/car_detail.html', context=context)


def manufacturercountry_list(request):
    manufacturercountry_list = ManufacturerCountry.objects.all()
    paginator = Paginator(manufacturercountry_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'manufacturercountry_list': page_obj
    }
    return render(request, 'shop/manufacturercountry_list.html', context=context)


def manufacturercountry_detail(request, manufacturercountry_id):
    manufacturercountry = get_object_or_404(ManufacturerCountry, id=manufacturercountry_id)
    context = {
        'manufacturercountry': manufacturercountry
    }
    return render(request, 'shop/manufacturercountry_detail.html', context=context)

#
# def color_list(request):
#     color_list = Color.objects.all()
#     paginator = Paginator(color_list, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'color_list': page_obj
#     }
#     return render(request, 'shop/color_list.html', context=context)
#
# #
# # def color_detail(request, color_id):
# #     color = get_object_or_404(Color, id=color_id)
# #     context = {
# #         'color': color
# #     }
# #     return render(request, 'shop/color_detail.html', context=context)


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = '/shop/'

class LoginRequiredColorMixin(LoginRequiredMixin):
    login_url = '/shop/login/'

class ColorListView(LoginRequiredColorMixin, ListView):
    model = Color
    template_name = 'shop/color_list.html'
    context_object_name = 'colors'
    paginate_by = 100000

    def get_colors_from_model(self):
        colors_queryset = Color.objects.all()
        data = list(colors_queryset.values_list('id', 'name'))
        cache.set("colors_list", data, timeout=300)

    def get(self, request, *args, **kwargs):
        self.get_colors_from_model()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_from_redis = cache.get("colors_list")

        if data_from_redis is not None:
            context['data_from_redis'] = data_from_redis
        else:
            colors_queryset = Color.objects.all()
            data = list(colors_queryset.values_list('id', 'name'))
            context['data_from_redis'] = data

        return context



class ColorCreateView(LoginRequiredColorMixin, CreateView):
    model = Color
    template_name = 'shop/color_create.html'
    fields = ['name']
    success_url = reverse_lazy('shop:color_list')

class ColorUpdateView(LoginRequiredColorMixin, UpdateView):
    model = Color
    template_name = 'shop/color_update.html'
    fields = ['name']
    success_url = reverse_lazy('shop:color_list')

class ColorDeleteView(LoginRequiredColorMixin, DeleteView):
    model = Color
    template_name = 'shop/color_delete.html'
    success_url = reverse_lazy('shop:color_list')

class ColorDetailView(LoginRequiredColorMixin, DetailView):
    model = Color
    template_name = 'shop/color_detail.html'
    context_object_name = 'color'