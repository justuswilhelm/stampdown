"""URLs for project."""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from .sitemaps import sitemaps

urlpatterns = (
    url(r"^admin/", admin.site.urls),
    url(r"^registration/", include("registration.urls")),
    url(r"^dashboard/", include("dashboard.urls", namespace="dashboard")),
    url(r"^", include("landing.urls", namespace="landing")),
    url(r"^robots\.txt$", TemplateView.as_view(template_name="robots.txt",
                                               content_type="text/plain"),
        name="robots"),
    url(r"^sitemap\.xml$", sitemap, {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"))

admin.site.site_header = _("{{ cookiecutter.project_name }} Admin")
admin.site.site_title = _("{{ cookiecutter.project_name }} Admin")
admin.site.index_title = _("{{ cookiecutter.project_name }} Admin")
