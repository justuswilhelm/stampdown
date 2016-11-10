"""Views for registration app."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


class UserDetailView(LoginRequiredMixin, DetailView):
    """DetailView for User."""

    template_name = "auth/user_detail.haml"

    def get_object(self):
        """Return User."""
        return self.request.user
