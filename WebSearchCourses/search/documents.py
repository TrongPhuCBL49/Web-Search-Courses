from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from course.models import Course

@registry.register_document
class CourseDocument(Document):
    class Index:
        name = 'courses'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Course

        fields = [
            'id', 
            'name', 
            'language',
            'level',
            'description', 
            'subject',
            'length', 
            'effort',
            'price', 
            'institution', 
            'about', 
            'content'
        ]