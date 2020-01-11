from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from . import views
urlpatterns = [
    path('', views.index),
    path('upload', views.handleUpload, name='upload'),
]
