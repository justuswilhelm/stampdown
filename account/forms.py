"""Forms for account app."""
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import UserProfile
from .signals import password_changed


User = get_user_model()


class UserCreationForm(auth_forms.UserCreationForm):
    """Override signup form."""

    email = forms.EmailField(
        label=_("Email Address"),
        widget=forms.TextInput(),
        required=True,
    )

    email_confirm = forms.EmailField(
        label=_("Email Address confirmation"),
        widget=forms.TextInput(),
        required=True,
    )

    def clean(self):
        """Override clean and validate email_confirm."""
        data = super().clean()
        if 'email' not in data:
            return data
        if 'email_confirm' not in data:
            return data
        if data['email'] != data['email_confirm']:
            msg = _(
                "Please confirm your email address",
            )
            self.add_error('email', msg)
            self.add_error('email_confirm', msg)

        return data

    def __init__(self, *args, **kwargs):
        """Delete username and make email identifier field."""
        super().__init__(*args, **kwargs)
        self.order_fields(("email", "email_confirm", "password1", "password2"))

    class Meta(auth_forms.UserCreationForm.Meta):
        """Extend Meta with EmailUser model."""

        # This line is important for email unique validation
        model = User
        fields = "email",


class UserProfileForm(forms.ModelForm):
    """."""

    class Meta:
        """."""

        model = UserProfile
        fields = ()


class AuthenticationForm(auth_forms.AuthenticationForm):
    """Override AuthenticationForm, username->email."""

    def __init__(self, *args, **kwargs):
        """Change label of username identifier field."""
        super().__init__(*args, **kwargs)


class PasswordResetForm(auth_forms.PasswordResetForm):
    """Override PasswordResetForm, use custom email template."""

    def send_mail(self, subject, obj, context, from_email, to_email, **kwargs):
        """Override send_email behavior."""
        raise NotImplementedError()


class SetPasswordForm(auth_forms.SetPasswordForm):
    """Override SetPasswordForm, fire user password changed signal."""

    def save(self, *args, **kwargs):
        """Fire password_changed signal."""
        user = super().save(*args, **kwargs)
        password_changed.send(sender=self.__class__, instance=user)
        return user
