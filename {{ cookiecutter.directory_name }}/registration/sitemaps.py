"""Sitemaps for registration."""
from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class RegistrationSitemap(sitemaps.Sitemap):
    """Provide sitemap for static pages in this app."""

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        """Return all items."""
        return ('login', 'logout', 'signup',
                'password_reset', 'password_reset_complete')

    def location(self, item):
        """Return URL for all items."""
        return reverse(item)
