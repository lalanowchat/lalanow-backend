from django.core.management.base import BaseCommand, CommandError
from app.django_orm.content import models as django_models
from app.django_orm.content.management.utils.create_messages import load_messages


class Command(BaseCommand):
    # https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/
    help = "Adds Message entries to the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # populate database with messages
        message_count = load_messages()
        self.stdout.write(
            self.style.SUCCESS(f"Created {message_count} messages in the database.")
        )
