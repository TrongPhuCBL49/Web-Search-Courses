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
    course_of_page = 3
    pageNo = request.POST.get('pageNo')
    pageSize = course_of_page
    search_text = request.POST.get('search_text')
    subject_text = request.POST.get('subject')
    language_text = request.POST.get('language')
    level_text = request.POST.get('level')
    institution_text = request.POST.get('institution')

    print('search_text', search_text)
    print('subject_text', subject_text)
    print('language_text', language_text)
    print('level_text', level_text)
    print('institution_text', institution_text)
    print('pageNo', pageNo)
    print('pageSize', pageSize)

    courses = Course.objects.all()
    courses_size = len(courses)
    subjects = Subject.objects.all()
    languages = Language.objects.all()
    levels = Level.objects.all()
    institutions = Institution.objects.all()

    if search_text is None:
        pageNo = 0
        pageSize = course_of_page
        courses = None
        courses_size = 0

    

    data = {
         'courses': courses,
         'courses_size': courses_size,
         'subjects': subjects,
         'languages': languages,
         'levels': levels,
         'institutions': institutions,
         'pageNo': pageNo,
         'pageSize': pageSize,
    }
    print(data)
    return render(request, 'search/courses.html', data)

def search2(request):
    return render(request, 'search/courses2.html')
