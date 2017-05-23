"""Landing app URLpatterns."""
from django.conf.urls import url

from .views import (
    FAQView,
    ImprintView,
    LandingView,
    TOSView,
)


urlpatterns = (
    url(r'^$', LandingView.as_view(), name='landing'),
    url(r"^faq/$", FAQView.as_view(), name="faq"),
    url(r"^imprint/$", ImprintView.as_view(), name="imprint"),
    url(r"^tos/$", TOSView.as_view(), name="tos"),
)
