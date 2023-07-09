from django.contrib import admin
from .models import Car, Color, Transmission, CarShop, ManufacturerCountry, Engine


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'body', 'engine', 'transmission', 'color', 'manufacture_date']
    list_filter = ['model', 'body', 'engine', 'transmission', 'color']
    search_fields = ['model']


@admin.register(CarShop)
class CarShopAdmin(admin.ModelAdmin):
    list_display = ['car', 'count', 'receipt_date']
    list_filter = ['car', 'count', 'receipt_date']
    search_fields = ['car']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['name']


class ManufacturerCountryInlineModelAdmin(admin.TabularInline):
    model = ManufacturerCountry
    fk_name = 'engine'


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ['name', 'power', 'type_engine']
    inlines = [ManufacturerCountryInlineModelAdmin]


@admin.register(ManufacturerCountry)
class ManufacturerCountryAdmin(admin.ModelAdmin):
    # list_display = ['engine', 'country']
    pass
