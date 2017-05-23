"""Models for account app."""
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(auth_models.BaseUserManager):
    """Copy of django.contrib.auth manager."""

    def _create_user(self, email, password, **kwargs):
        """Create and save a user with email, and password."""
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.clean()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        """Createa a superuser."""
        return self._create_user(
            email=email,
            password=password,
            **kwargs,
        )

    def create_superuser(self, email, password, **kwargs):
        """Createa a superuser."""
        return self._create_user(
            email=email,
            password=password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            **kwargs,
        )


class EmailUser(auth_models.AbstractBaseUser):
    """User model with Email."""

    is_superuser = models.BooleanField(
        verbose_name=_('Superuser'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    email = models.EmailField(
        verbose_name=_('Email address'),
        unique=True,
    )
    is_staff = models.BooleanField(
        verbose_name=_('Staff'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date Joined'),
        auto_now_add=True
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        """Meta."""

        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def clean(self):
        """Clean."""
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """Return first letter of email."""
        return self.get_short_name()

    def get_short_name(self):
        """Return first letter of email."""
        return self.email[0].upper() + "."

    def has_perm(self, perm, obj=None):
        """User has all perms given that they are a superuser."""
        return self.is_superuser

    def has_perms(self, perms, obj=None):
        """User has all perms given that they are a superuser."""
        return self.is_superuser

    def has_module_perms(self, perm):
        """User has all perms given that they are a superuser."""
        return self.is_superuser


class UserProfile(models.Model):
    """UserProfile."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    class Meta:
        """Meta."""

        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")
