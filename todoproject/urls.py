from django.contrib import admin
from django.urls import path, include # couese-29

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')), # couese-29
]
