from django.contrib import admin
from .models import Language, Level, Subject, Course
# Register your models here.

admin.site.register(Language)
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Course)