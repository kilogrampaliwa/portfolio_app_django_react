# backend/api_urls.py
from django.urls import path, include
from django.http import JsonResponse


urlpatterns = [
    path('', include('technologies.urls')),
]
