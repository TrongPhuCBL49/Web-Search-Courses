import json

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Run file import-data ok")
        with open("edx_course_data.json") as f:
            data = json.load(f)

        for course in data:
            print(course['name'])
