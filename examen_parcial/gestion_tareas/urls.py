from unicodedata import name
from django.contrib import admin
from django.urls import path
from gestion_tareas import views 

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
]