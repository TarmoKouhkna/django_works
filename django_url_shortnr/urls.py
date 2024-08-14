# django_url_shortnr/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortener_app.urls')),  # Include URLs from shortener_app
]
