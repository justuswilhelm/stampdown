"""Sitemaps for registration."""
from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class DashboardSitemap(sitemaps.Sitemap):
    """Provide sitemap for static pages in this app."""

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        """Return all items."""
        return "dashboard:dashboard",

    def location(self, item):
        """Return URL for all items."""
        return reverse(item)
