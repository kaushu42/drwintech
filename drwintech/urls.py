from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('app.urls')),
]
