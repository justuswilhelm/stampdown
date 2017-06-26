"""Timestamp models."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from common import models as common_models


class Timestamp(common_models.UserModel):
    """Timestamp with comment and other goodies."""

    value = models.DateTimeField(
        verbose_name=_("value"),)
    comment = models.TextField(
        verbose_name=_("comment"),
    )