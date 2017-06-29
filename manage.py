#!/usr/bin/env python
"""Manage.py."""
import os
import sys

from dotenv import (
    find_dotenv,
    load_dotenv,
)


if __name__ == "__main__":  # pragma: no cover
    load_dotenv(find_dotenv())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stampdown.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
