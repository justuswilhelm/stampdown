"""Timestamp Admin."""
from django.contrib import admin
from django.utils.timezone import now

from .models import Timestamp


@admin.register(Timestamp)
class TimestampAdmin(admin.ModelAdmin):
    """ModelAdmin for Timestamp."""

    def get_form(self, request, obj=None, **kwargs):
        """Prepopulate date time with current."""
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['value'].initial = now()
        form.base_fields['user'].initial = request.user
        return form
