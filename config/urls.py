from django.contrib import admin
from django.urls import path
from django.urls import include
from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("HELLO")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro/', include('intro.urls')),
    path('', include('intro.urls')),
]
