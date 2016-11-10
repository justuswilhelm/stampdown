#!/usr/bin/env python
"""Manage.py."""
import os
import sys
from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "{{ cookiecutter.directory_name }}.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
