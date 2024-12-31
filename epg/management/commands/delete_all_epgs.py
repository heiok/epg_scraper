from django.core.management.base import BaseCommand
from epg.models import EPG

class Command(BaseCommand):
    help = 'Delete all EPG data'

    def handle(self, *args, **kwargs):
        EPG.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all EPG data'))

