from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'about.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)

