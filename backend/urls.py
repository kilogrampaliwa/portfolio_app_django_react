from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

index_view = never_cache(TemplateView.as_view(template_name="index.html"))

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("backend.api_urls")),
    static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, 'frontend/build/static'))
]

if settings.DEBUG:
    urlpatterns += static('/images/', document_root=os.path.join(BASE_DIR, 'frontend/build/images'))
    urlpatterns += static('/gifs/', document_root=os.path.join(BASE_DIR, 'frontend/build/gifs'))

urlpatterns += [
#urlpatterns += [
#    re_path(r'^(?!favicon\.ico$).*$', index_view),
#]
]
