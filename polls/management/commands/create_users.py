from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from faker import Faker
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create random users '

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='number of users')

    def handle(self, *args, **options):
        count = options['count']

        if count < 1 or 10 < count:
            raise ValidationError('Count must be between 1 and 10')

        faker = Faker()
        users = []

        for i in range(count):
            username = faker.user_name()
            email = faker.email()
            password = faker.password()

            user = User(username=username, email=email)
            user.set_password(password)

            users.append(user)

        User.objects.bulk_create(users)




