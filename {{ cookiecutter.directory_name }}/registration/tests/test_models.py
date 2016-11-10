"""Model tests for registration app."""
from django.test import TestCase

from ..factories import SuperUserFactory


class UserTestCase(TestCase):
    """Test User and connected models."""

    def test_super_user_factory(self):
        """Factory will set a password."""
        params = {'email': 'name@domain.com', 'password': 'password',
                  'username': 'name@domain.com'}
        SuperUserFactory(**params)
        self.assertTrue(self.client.login(**params))
