from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse ("<h1> Первая страница моего проекта на Джанго </h1>")

def news (request):
    return HttpResponse ("<h1> Вторая страница моего проекта на Джанго </h1>")


def data (request):
    return HttpResponse ("<h1> Это DATA страница моего проекта на Джанго </h1>")


def test (request):
    return HttpResponse ("<h1> Это TEST страница моего проекта на Джанго </h1>")

