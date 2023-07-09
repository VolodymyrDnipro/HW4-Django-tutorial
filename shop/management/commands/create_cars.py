from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from mimesis import Transport
from faker import Faker
from shop.models import Color, Transmission, Engine, Car, CarShop, ManufacturerCountry
from datetime import datetime, timedelta
import random, string


class Command(BaseCommand):
    help = 'Create random cars '

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count of cars')

    def handle(self, *args, **options):
        count = options['count']

        if count < 1:
            raise ValidationError('Count must be > 1')

        car_body = ['sedan', 'hatchback', 'crossover', 'convertible', 'truck', 'minivan']
        transmissions = ['automatic', 'manual', 'robotic']
        type_engines = ['Diesel', 'Hybrid', 'Petrol', 'Electric', 'Gas']

        transport = Transport()
        fake = Faker()
        today = datetime.now().date()

        for i in range(count):
            model = transport.car()
            country = fake.country()
            body = random.choice(car_body)
            random_color = fake.color_name()
            transmission = random.choice(transmissions)
            type_engine = random.choice(type_engines)
            engine_model = ''.join(random.choices(string.ascii_uppercase, k=4))
            engine_power = random.randint(150, 400)
            car_count = random.randint(1, 10)
            random_days = random.randint(1, 10000)
            manufacture_date = today - timedelta(days=random_days)

            car_color = Color.objects.create(name=random_color)
            car_transmission = Transmission.objects.create(name=transmission)
            car_engine = Engine.objects.create(name=engine_model, power=engine_power, type_engine=type_engine)
            manufacturer_country = ManufacturerCountry.objects.create(engine=car_engine, country=country)

            car = Car.objects.create(
                model=model,
                body=body,
                engine=car_engine,
                transmission=car_transmission,
                color=car_color,
                manufacture_date=manufacture_date
            )

            car_shop = CarShop.objects.create(car=car, count=car_count)

            car_color.save()
            car_transmission.save()
            car_engine.save()
            manufacturer_country.save()
            car.save()
            car_shop.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} cars'))
