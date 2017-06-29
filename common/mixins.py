"""View Mixins and Base Classes for Stampdown."""
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


class SuperUserMixin(UserPassesTestMixin):
    """Mixin that only lets superusers in."""

    def test_func(self):
        """Assert user is superuser."""
        return self.request.user.is_superuser


class AnonymousRequiredMixin(UserPassesTestMixin):
    """Mixin that only lets anonymous users in."""

    login_url = reverse_lazy('dashboard:dashboard')

    def test_func(self):
        """Assert user is anonymous."""
        return self.request.user.is_anonymous()
