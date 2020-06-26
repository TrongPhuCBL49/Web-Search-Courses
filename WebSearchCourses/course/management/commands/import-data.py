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
        self.import_course()
    
    def import_language(self):
        print("Start import Languages")
        languages = {"English"}
        for course in data:
            for language in course['language']:
                languages.add(language)
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
        for name in subjects:
            if not Subject.objects.filter(name=name).exists():
                Subject.objects.create(name=name)
        print("Import subjects done")

    def import_course(self):
        print("Start import courses")
        for course in data:
            name        = course['name']
            languages   = [Language.objects.filter(name=name)[0] for name in course['language']]
            levels      = [Level.objects.filter(name=name)[0] for name in course['level']]
            description = course['description']
            subjects    = [Subject.objects.filter(name=name)[0] for name in course['subjects']]
            length      = course['length']
            effort      = course['effort']
            price       = course['price']
            institution = course['institution']
            about       = course['about-course']
            content     = course['content-course']
            link_image  = course['link-image']
            if not Course.objects.filter(name=name, length=length).exists():
                new_course = Course(
                    name=name,
                    description=description,
                    length=length,
                    effort=effort,
                    price=price,
                    institution=institution,
                    about=about,
                    content=content,
                    link_image=link_image
                )
                new_course.save()
                for language in languages:
                    new_course.language.add(language)
                for level in levels:
                    new_course.level.add(level)
                for subject in subjects:
                    new_course.subject.add(subject)
        print("Import courses done")
        