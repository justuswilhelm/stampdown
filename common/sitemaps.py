"""Sitemaps for Stampdown."""
from django.contrib import sitemaps
from django.urls import reverse

from account.sitemaps import AccountSitemap
from dashboard.sitemaps import DashboardSitemap


class StaticViewSitemap(sitemaps.Sitemap):
    """Sitemap for static views in this app."""

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        """Provide names of static pages."""
        return 'robots',

    def location(self, item):
        """Provide urls of static pages."""
        return reverse(f'common:{item}')


sitemaps = {
    'account': AccountSitemap(),
    'dashboard': DashboardSitemap(),
    'static': StaticViewSitemap(),
}
