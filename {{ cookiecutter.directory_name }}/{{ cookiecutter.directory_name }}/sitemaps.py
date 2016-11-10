"""Sitemaps for {{ cookiecutter.project_name }}."""
from django.contrib import sitemaps
from django.core.urlresolvers import reverse

from dashboard.sitemaps import DashboardSitemap
from registration.sitemaps import RegistrationSitemap


class StaticViewSitemap(sitemaps.Sitemap):
    """Sitemap for static views in this app."""

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        """Provide names of static pages."""
        return 'robots',

    def location(self, item):
        """Provide urls of static pages."""
        return reverse(item)


sitemaps = {'static': StaticViewSitemap(),
            'registration': RegistrationSitemap(),
            'dashboard': DashboardSitemap()}
