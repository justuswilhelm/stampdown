"""Dashboard app views."""
from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    """Dashboard View."""

    template_name = 'dashboard/dashboard.haml'
