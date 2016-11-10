"""Landing App views."""
from django.views.generic.base import TemplateView


class LandingView(TemplateView):
    """What an anonymous user will see."""

    template_name = 'landing/landing.haml'


class FAQView(TemplateView):
    """FAQ for our users."""

    template_name = 'landing/faq.haml'


class TOSView(TemplateView):
    """TOS for our users."""

    template_name = 'landing/tos.haml'


class ImprintView(TemplateView):
    """TOS for our users."""

    template_name = 'landing/imprint.haml'
