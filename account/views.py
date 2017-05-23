"""Views for registration app."""
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    FormView,
    TemplateView,
)

from .forms import UserCreationForm


class SignupView(FormView):
    """Sign Up View."""

    form_class = UserCreationForm
    success_url = reverse_lazy('account:signup_done')
    template_name = 'account/signup.haml'

    def form_valid(self, form):
        """."""
        self.create_user(form)
        return super().form_valid(form)

    def create_user(self, form, **kwargs):
        """Create user from form data."""
        return get_user_model().objects.create_user(
            password=form.cleaned_data["password1"],
            email=form.cleaned_data["email"],
        )


class UserDetailView(LoginRequiredMixin, DetailView):
    """DetailView for User."""

    template_name = "account/user_detail.haml"

    def get_object(self):
        """Return User."""
        return self.request.user


class SignupDoneView(TemplateView):
    """Signup Done."""

    template_name = "account/signup_done.haml"
