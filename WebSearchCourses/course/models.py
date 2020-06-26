from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save

from WebSearchCourses.utils import unique_slug_generator
# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Course(models.Model):
    name        = models.TextField(blank=True, null=True)
    language    = models.ManyToManyField(Language, blank=True)
    level       = models.ManyToManyField(Level, blank=True)
    description = models.TextField(blank=True, null=True)
    subject     = models.ManyToManyField(Subject, blank=True)
    length      = models.CharField(max_length=255, blank=True, null=True)
    effort      = models.CharField(max_length=255, blank=True, null=True)
    price       = models.CharField(max_length=255, blank=True, null=True)
    institution = models.CharField(max_length=255, blank=True, null=True)
    about       = models.TextField(blank=True, null=True)
    content     = models.TextField(blank=True, null=True)
    link_image  = models.SlugField(blank=True, null=True)
    slug        = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        # return "/products/{slug}".format(slug=self.slug)
        return reverse("course:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

def course_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(course_pre_save_receiver, sender=Course)