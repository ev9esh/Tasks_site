from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('about/', views.about, name='about'),
        path('my_template/', views.my_template, name='my'),
]