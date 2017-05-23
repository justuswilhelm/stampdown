"""Test common management."""
import pytest
from django.core.management import call_command


@pytest.mark.django_db
def test_seeddb():
    """Test seeddb management command."""
    call_command('seeddb')
