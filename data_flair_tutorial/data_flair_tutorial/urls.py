"""data_flair_tutorial URL Configuration

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
from django.urls import path

from django.conf.urls import include
from .views import *

from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('login/', include('login.urls')),
    path('dataflair/', index),
    path('redirect/', data_flair),
    path('djangotutor/', tutorial.as_view()),
    path('setcookie/', setcookie),
    path('getcookie/', showcookie),
    path('deletecookie/', delete_co),
    # path('djangotutor/', RedirectView.as_view(url = 'https://data-flair.training/blogs/category/django/')),
]
