from django.urls import path

from .views import search, search2

app_name = 'search'

urlpatterns = [
    path('', search, name='home'),
    path('search2/', search2, name='search2'),
]
