from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Crawl data from website"

    def handle(self, *args, **options):
        print("Run command ok!")
        #return super().handle(*args, **options)