"""Dashboard app views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from timestamp.models import Category


class DashboardView(LoginRequiredMixin, TemplateView):
    """Dashboard View."""

    template_name = 'dashboard/dashboard.haml'

    def get_context_data(self, **kwargs):
        """Enrich context with categories."""
        return {
            **super().get_context_data(**kwargs),
            'categories': Category.objects.all(),
        }
