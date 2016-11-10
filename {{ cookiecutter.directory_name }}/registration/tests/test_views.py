"""Tests for registration app."""
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase
from nose.tools import eq_

User = get_user_model()


class LoginTestCase(TestCase):
    """Test LoginView."""

    url = reverse("login")
    valid_credentials = {'username': 'username', 'password': 'password'}

    def test_login_get(self):
        """Get gives us 200."""
        response = self.client.get(self.url)
        eq_(response.status_code, 200)

    def test_login_post_with_invalid_credentials(self):
        """Posting invalid credentials results in a 200."""
        response = self.client.post(self.url)
        eq_(response.status_code, 200)

    def test_login_post_with_valid_credentials(self):
        """Posting valid credentials results in a 302."""
        User.objects.create_user(email='email@domain.com',
                                 **self.valid_credentials)
        response = self.client.post(self.url, self.valid_credentials)
        eq_(response.status_code, 302, response.content)
        response = self.client.get(response.url)
