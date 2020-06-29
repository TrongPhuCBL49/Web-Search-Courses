from django.urls import path

from .views import search, search2, CourseDetailSlugView

app_name = 'search'

urlpatterns = [
    path('', search, name='home'),
    path('<slug:slug>/', CourseDetailSlugView.as_view(), name='detail'),
    path('search2/', search2, name='search2'),
]
