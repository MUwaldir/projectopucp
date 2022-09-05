
from django.contrib import admin
from django.urls import path
from gestion_tareas import views

app_name = 'gestion_tareas'
urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('crear', views.crear, name='vista_creacion'),
    path('editar/<int:tareas_id>', views.editar, name='vista_edicion'),
    path('delete/<int:tareas_id>', views.delete, name='delete'),
    path('detalle/<int:tareas_id>', views.detalle, name='vista_detallada'),
    
]