from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'about.html')


def create(request):
    return render(request, 'create.html')
