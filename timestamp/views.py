"""Timestamp Views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic.edit import CreateView

from .models import Timestamp


class TimestampCreateView(LoginRequiredMixin, CreateView):
    """Timestamp CreateView."""

    fields = 'comment',
    model = Timestamp
    success_url = reverse_lazy('dashboard:dashboard')
    template_name = "timestamp/timestamp_form.haml"

    def form_valid(self, form):
        """Assign user and current time to timestamp."""
        timestamp = form.save(commit=False)
        timestamp.value = now()
        timestamp.user = self.request.user
        return super().form_valid(form)
