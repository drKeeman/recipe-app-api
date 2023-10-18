"""
Django command to wait to DB to be avaliable
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for DB"""

    def handle(self, *argsm, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("DB unavaliable, waiting 1 sec...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database avaliable!"))
