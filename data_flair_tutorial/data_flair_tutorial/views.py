from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView

def index(request):
    html = '<h1>Data Flair Django</h1>Hello, you just configured you First URL'
    return HttpResponse(html)

def data_flair(request):
    return redirect('/dataflair')

class tutorial(RedirectView): url = 'https://data-flair.training/blogs/category/django/'