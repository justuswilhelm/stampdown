"""Project view tests."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_sitemap(client):
    """Test sitemap retrieval."""
    response = client.get(reverse('common:sitemap'))
    assert response.status_code == 200
