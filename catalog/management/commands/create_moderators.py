from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Модераторы')

        # Добавляем права
        permissions = Permission.objects.filter(
            codename__in=[
                'delete_product',
                'can_publish_product',
                'can_unpublish_product'
            ]
        )
        group.permissions.set(permissions)

        self.stdout.write('Группа модераторов создана')