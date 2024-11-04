from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'main/index.html', {'caption':"CatDjango"})

def news (request):
    return render (request, 'main/news.html')


def data (request):
    return render (request, 'main/data.html')


def test (request):
    return render (request, 'main/test.html')

