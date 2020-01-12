from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from . import views
urlpatterns = [
    path('', views.index, name='upload'),
    path('skills', views.skills, name='skills'),
    path('people', views.people, name='people'),
]
