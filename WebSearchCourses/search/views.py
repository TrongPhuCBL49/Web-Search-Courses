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
    pageSize = 6

    pageNo = request.POST.get('pageNo')
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
    # courses = Course.objects.all()

    if search_text:
        courses = Course.objects.all()
        search_courses = courses
        # search_courses = CourseDocument.search().query('match', name=search_text).to_queryset()
        # search_courses = CourseDocument.search().filter('term', language=language_text).to_queryset()
        # courses = search_courses[(int(pageNo)-1)*int(pageSize):int(pageNo)*int(pageSize)]
    else:
        courses = []
        search_courses = []

    courses_size = len(search_courses)
    subjects = Subject.objects.all()
    languages = Language.objects.all()
    levels = Level.objects.all()
    institutions = Institution.objects.all()

    if search_text is None:
        pageNo = 0
        # courses = None
        # courses_size = 0

    data = {
         'courses': courses,
         'search_text': search_text,
         'subject_text': subject_text,
         'level_text': level_text,
         'language_text': language_text,
         'institution_text': institution_text,
         'courses_size': courses_size,
         'subjects': subjects,
         'languages': languages,
         'levels': levels,
         'institutions': institutions,
         'pageNo': pageNo,
         'pageSize': pageSize,
    }
    print('data', data)
    return render(request, 'search/courses.html', data)

def search2(request):
    return render(request, 'search/courses2.html')
