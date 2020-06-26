import json

from django.core.management.base import BaseCommand
from course.models import Language, Level, Subject, Course

with open("edx_course_data.json") as f:
    data = json.load(f)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Running import-data command")
        self.import_language()
        self.import_level()
        self.import_subject()
    
    def import_language(self):
        print("Start import Languages")
        languages = {"English"}
        for course in data:
            for language in course['language']:
                languages.add(language)
        print(languages)
        for name in languages:
            if not Language.objects.filter(name=name).exists():
                Language.objects.create(name=name)
        print("Import Languages done")

    def import_level(self):
        print("Start import Levels")
        levels = {"Introductory"}
        for course in data:
            for level in course['level']:
                levels.add(level)
        print(levels)
        for name in levels:
            if not Level.objects.filter(name=name).exists():
                Level.objects.create(name=name)
        print("Import Levels done")

    def import_subject(self):
        print("Start import subjects")
        subjects = {"Humanities"}
        for course in data:
            for subject in course['subjects']:
                subjects.add(subject)
        print(subjects)
        for name in subjects:
            if not Subject.objects.filter(name=name).exists():
                Subject.objects.create(name=name)
        print("Import subjects done")