"""Admin modules for registration app."""
from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """UserProfile admin."""

    list_display = 'user',

    def get_queryset(self, request):
        """Prefetch ratings and comments."""
        return super().get_queryset(request).select_related('user')
