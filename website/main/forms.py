from .models import Task
from django.forms import ModelForm, widgets, TextInput
from dataclasses import fields


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ведите название'}),
                   'task': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ведите описание'}),
                   }
