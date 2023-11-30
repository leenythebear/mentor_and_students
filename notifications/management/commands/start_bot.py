from django.core.management import BaseCommand

from notifications.telegram import start_bot


class Command(BaseCommand):
    help = 'Телеграм бот'

    def handle(self, *args, **options):
        start_bot()
