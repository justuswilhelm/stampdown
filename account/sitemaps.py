"""Sitemaps for account."""
from django.contrib import sitemaps
from django.urls import reverse


class AccountSitemap(sitemaps.Sitemap):
    """Provide sitemap for static pages in this app."""

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        """Return all items."""
        return (
            'login',
            'logout',
            'password_reset',
            'password_reset_complete',
            'signup',
        )

    def location(self, item):
        """Return URL for all items."""
        return reverse(f'account:{item}')
