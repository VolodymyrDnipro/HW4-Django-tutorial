from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Delete users '

    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int, help='User to delete')

    def handle(self, *args, **options):
        user_ids = options['user_ids']
        print(user_ids)

        for user_id in user_ids:
            user = User.objects.get(id=user_id)
            if user.is_superuser:
                self.stderr.write(f'Cannot delete id: {user_id} its superuser.')
                return

        User.objects.filter(id__in=user_ids).delete()
