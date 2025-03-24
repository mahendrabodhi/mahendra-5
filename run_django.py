INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Add this line
]

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp.views import home

urlpatterns = [
    path('', home),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
