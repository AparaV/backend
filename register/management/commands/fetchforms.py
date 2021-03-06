from django.core.management.base import BaseCommand
from register import forms


class Command(BaseCommand):
    help = 'Fetches last forms from Typeform'

    def handle(self, *args, **options):
        fetched = forms.ApplicationsTypeform().update_forms()
        self.stdout.write(self.style.SUCCESS('Successfully fetched %s forms"' % len(fetched)))
