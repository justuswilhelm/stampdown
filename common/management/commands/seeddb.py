"""Seed the db."""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from timestamp.models import Category


User = get_user_model()


class Command(BaseCommand):
    """Seed the db."""

    def create_categories(self):
        """Create timestamp categories."""
        Category.objects.bulk_create(
            [
                Category(name="Return Home"),
                Category(name="Leave Home"),
            ]
        )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Handle command invocation."""
        User.objects.create_superuser(
            email='justus@justus.justus',
            password=settings.SECRET_KEY,
        )
        self.create_categories()
