"""Admin modules for account app."""
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import UserProfile


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """UserAdmin for our EmailUser."""

    list_display = 'email', 'is_staff', 'is_superuser'
    list_filter = 'is_staff', 'is_superuser', 'is_active'
    search_fields = 'email',
    ordering = 'email',
    filter_horizontal = ()
    fieldsets = (
        (
            "",
            {
                'fields': (
                    'email',
                    'password',
                ),
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """UserProfile admin."""

    list_display = 'user',

    def get_queryset(self, request):
        """Prefetch ratings and comments."""
        return super().get_queryset(request).select_related('user')
