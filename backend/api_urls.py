# backend/api_urls.py
from django.urls import path, include
from django.http import JsonResponse

def test_api(request):
    return JsonResponse({'message': 'API działa!'})

urlpatterns = [
    path('test/', test_api),
    path('', include('technologies.urls')),
]
