"""Test Account models."""
import pytest
from django.contrib.auth import authenticate


class TestUser:
    """Test user."""

    def test_anonymize(self, user):
        """It anonymizes a user."""
        user.email = 'weird@al.yankovic'
        assert user.get_short_name() == 'W.'
        assert user.get_full_name() == 'W.'

    def test_naughty_character(self, user):
        """It anonymizes a user."""
        user.email = '😎eird@al.yankovic'
        assert user.get_short_name() == '😎.'
        assert user.get_full_name() == '😎.'

    def test_perms(self, user):
        """A regular user is quite powerless."""
        assert not user.has_perm('')
        assert not user.has_perms([])
        assert not user.has_module_perms('')

    def test_staff_perms(self, user):
        """A staff user is quite benign."""
        user.is_staff = True
        assert not user.has_perm('')
        assert not user.has_perms([])
        assert not user.has_module_perms('')

    def test_superuserperms(self, user):
        """A regular user is quite powerless."""
        user.is_staff = True
        user.is_superuser = True
        assert user.has_perm('')
        assert user.has_perms([])
        assert user.has_module_perms('')


@pytest.mark.django_db
class TestUserManager:
    """Test UserManager."""

    def test_create_user(self, db_user, user_credentials):
        """Test create_user."""
        assert not db_user.is_superuser
        assert not db_user.is_staff
        assert db_user.check_password(user_credentials['password'])
        assert authenticate(**user_credentials) == db_user

    def test_create_superuser(self, db_superuser, user_credentials):
        """Test superuser creation."""
        assert db_superuser.is_superuser
        assert db_superuser.is_staff
        assert db_superuser.check_password(user_credentials['password'])
