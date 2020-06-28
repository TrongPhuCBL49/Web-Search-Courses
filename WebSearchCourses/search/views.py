from django.shortcuts import render, redirect
from .documents import CourseDocument
from course.models import Course, Language, Subject, Level, Institution
# Create your views here.

# def search(request):
#     q = request.GET.get('q')
#     if q:
#         courses = CourseDocument.search().query('match', name=q)
#     else:
#         courses = ''

#     return render(request, 'search/search.html', {'courses': courses})

def search(request):
    #course_of_page = 30
    #pageNo = request.GET.get('pageNo')
    #pageSize = request.GET.get('pageSize')
    courses = Course.objects.all()
    subjects = Subject.objects.all()
    languages = Language.objects.all()
    levels = Level.objects.all()
    institutions = Institution.objects.all()
    data = {
         'courses': courses,
         'courses_size': len(courses),
         'subjects': subjects,
         'languages': languages,
         'levels': levels,
         'institutions': institutions,
    }
    return render(request, 'search/courses.html', data)

def search2(request):
    return render(request, 'search/courses2.html')
