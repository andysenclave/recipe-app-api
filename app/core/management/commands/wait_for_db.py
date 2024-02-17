"""
Django command to wait fo the database to be available before starting app
"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        pass