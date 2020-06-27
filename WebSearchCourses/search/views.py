from django.shortcuts import render
from .documents import CourseDocument
from course.models import Course
# Create your views here.

# def search(request):
#     q = request.GET.get('q')
#     if q:
#         courses = CourseDocument.search().query('match', name=q)
#     else:
#         courses = ''

#     return render(request, 'search/search.html', {'courses': courses})

def search(request):
    courses = Course.objects.all()
    
    data = {'courses': courses, 'size': len(courses)}
    return render(request, 'search/courses.html', data)

def search2(request):
    return render(request, 'search/courses2.html')
