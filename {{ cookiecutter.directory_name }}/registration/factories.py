"""Factory for registration app."""
from django.contrib.auth import get_user_model
from factory import Faker, SubFactory, make_factory, post_generation
from factory.django import DjangoModelFactory

from .models import UserProfile

User = get_user_model()

UserFactory = make_factory(User,
                           email=Faker('email'),
                           is_active=True,
                           username=Faker('user_name'),
                           first_name=Faker('first_name'),
                           last_name=Faker('last_name'),
                           FACTORY_CLASS=DjangoModelFactory)

UserProfileFactory = make_factory(UserProfile,
                                  user=SubFactory(UserFactory),
                                  FACTORY_CLASS=DjangoModelFactory)


class SuperUserFactory(UserFactory):
    """Provide pw override."""

    is_superuser = True
    is_staff = True

    @post_generation
    def password(self, create, extracted, **kwargs):
        """Assign password."""
        if extracted:
            self.set_password(extracted)
            self.save()
