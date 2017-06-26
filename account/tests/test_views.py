"""Tests for registration app."""
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


@pytest.mark.django_db
class TestLoginTestCase:
    """Test LoginView."""

    @pytest.fixture
    def resource_url(self):
        """URL to resource."""
        return reverse("account:login")

    def test_login_get(self, client, resource_url):
        """Get gives us 200."""
        response = client.get(resource_url)
        assert response.status_code == 200

    def test_login_post_invalid(self, client, resource_url):
        """Posting invalid credentials results in a 200."""
        response = client.post(resource_url)
        assert response.status_code == 200

    def test_login_post(self, client, user_credentials, db_user, resource_url):
        """Posting valid credentials results in a 302."""
        response = client.post(
            resource_url,
            {
                'username': db_user.email,
                'password': user_credentials['password'],
            },
        )
        assert response.status_code == 302


@pytest.mark.django_db
class TestSignup:
    """Test SignupFinishView."""

    resource_url = reverse("account:signup")

    @pytest.fixture
    def valid_data(self):
        """Return valid signup finish data."""
        return {
            'email': 'user@domain.com',
            'email_confirm': 'user@domain.com',
            'password1': 'securepassword',
            'password2': 'securepassword',
        }

    def test_get(self, client):
        """GET."""
        response = client.get(self.resource_url)
        assert response.status_code == 200

    def test_post(self, client, valid_data):
        """Assert user can be created."""
        response = client.post(self.resource_url, valid_data)
        print(response.context)
        assert response.status_code == 302


@pytest.mark.django_db
class TestUserDetailView:
    """Test UserDetailView."""

    resource_url = reverse('account:user_detail')

    def test_get(self, user_client):
        """Test GET."""
        response = user_client.get(self.resource_url)
        assert response.status_code == 200

    def test_get_anonymous(self, client):
        """Test GET."""
        response = client.get(self.resource_url)
        assert response.status_code == 302
