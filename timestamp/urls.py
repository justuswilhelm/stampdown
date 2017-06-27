"""Timestamp URLpatterns."""
from django.conf.urls import url

from .views import TimestampCreateView


urlpatterns = (
    url(
        r'^create/$',
        TimestampCreateView.as_view(),
        name='timestamp_create',
    ),
)
