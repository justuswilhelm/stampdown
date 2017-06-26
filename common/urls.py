"""Common urls."""
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from .sitemaps import sitemaps


urlpatterns = (
    url(
        r"^sitemap\.xml$",
        sitemap,
        {
            "sitemaps": sitemaps,
        },
        name="sitemap",
    ),
    url(
        r"^robots\.txt$",
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain",
        ),
        name="robots",
    ),
)
