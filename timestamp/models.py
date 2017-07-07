"""Timestamp models."""
from datetime import timedelta

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from common import models as common_models


class Category(common_models.StringNameModel):
    """Category for time stamps."""


class TimestampManager(models.Manager):
    """Manager for Timestamp."""

    def recent(self, days=7):
        """Return recent timestamps."""
        past = now() - timedelta(days=days)
        return self.filter(value__gt=past)


class Timestamp(common_models.UserModel):
    """Timestamp with comment and other goodies."""

    value = models.DateTimeField(
        verbose_name=_("value"),)
    comment = models.TextField(
        verbose_name=_("comment"),
    )
    category = models.ForeignKey(
        Category,
        null=True,
    )

    objects = TimestampManager()

    class Meta:
        """Model Meta."""

        ordering = (
            '-value',
        )
