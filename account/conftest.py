"""Account ConfTest."""
import pytest
from django.contrib.auth import get_user_model

from .models import UserProfile


User = get_user_model()


@pytest.fixture
def user():
    """Build user."""
    return User()


@pytest.fixture
def user_credentials():
    """Valid user credentials."""
    return {
        'email': 'user@example.com',
        'password': 'password',
    }


@pytest.mark.django_db
@pytest.fixture
def db_user(user_credentials):
    """Create user."""
    user = User.objects.create_user(**user_credentials, is_active=True)
    UserProfile.objects.create(user=user)
    return user


@pytest.mark.django_db
@pytest.fixture
def db_superuser(user_credentials):
    """Create super user."""
    user = User.objects.create_superuser(**user_credentials)
    UserProfile.objects.create(user=user)
    return user


@pytest.fixture
def user_client(client, db_user):
    """Create client with logged in user."""
    client.force_login(db_user)
    return client
