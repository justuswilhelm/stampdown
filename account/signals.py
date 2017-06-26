"""Account signals."""
from django.dispatch import Signal


password_changed = Signal(providing_args=["instance"])
