from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': "Курсы", 'url_name': 'prog'}]


# Create your views here.
def index(request):
    return render(request, 'main/home.html')


def prog(request):
    posts = courses.objects.all()
    return render(request, 'main/prog.html', {'posts': posts})


def quest(request):
    return render(request, 'main/quest.html')


def reg(request):
    return render(request, 'main/reg.html')


def login(request):
    return render(request, 'main/login.html')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_prog(request, courses_id):
    return HttpResponse(f"Отображение курса с id = {courses_id}")
