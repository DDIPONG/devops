"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def empty_view(request):
    return HttpResponse("Empty View")


##from bookmark.views import BookmarkLV, BookmarkDV -------Removed

urlpatterns = [
    path('', empty_view, name='empty view'),
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),


    #class-based views
    #path('bookmark/', BookmarkLV.as_view(), name='index'),
    #path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
