from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'gestion_tareas/login.html')


def dashboard(request):
    return render(request, 'gestion_tareas/dashboard.html')