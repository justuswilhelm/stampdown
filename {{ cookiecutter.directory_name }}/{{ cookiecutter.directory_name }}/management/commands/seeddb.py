"""Seed the db."""
from os import environ

from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db import transaction

from registration.factories import SuperUserFactory


class Command(BaseCommand):
    """Seed the db."""

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Handle command invocation."""
        Site.objects.create(domain='localhost:8000', name='Django Project')
        user = SuperUserFactory(username='justusperlwitz',
                                email='justus@justus.justus',
                                first_name='Justus',
                                last_name='Perlwitz')
        user.set_password(environ['SECRET_KEY'])
        user.save()
