"""Models for registration app."""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    """UserProfile."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        """Stringify."""
        return _("Profile of '{}'").format(self.user)
