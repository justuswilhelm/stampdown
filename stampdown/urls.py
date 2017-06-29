"""URLs for this project."""
from django.conf.urls import (
    include,
    url,
)
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


urlpatterns = (
    url(r"^", include("landing.urls", namespace="landing")),
    url(r"^/", include("common.urls", namespace="common")),
    url(r"^account/", include("account.urls", namespace="account")),
    url(r"^admin/", admin.site.urls),
    url(r"^dashboard/", include("dashboard.urls", namespace="dashboard")),
    url(r"^timestamp/", include("timestamp.urls", namespace="timestamp")),
    url(r'^tz_detect/', include('tz_detect.urls')),
)

admin.site.site_header = _("Admin")
admin.site.site_title = _("Admin")
admin.site.index_title = _("Admin")
