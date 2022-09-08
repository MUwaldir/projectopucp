import datetime
from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=128, default='')
    papellido = models.CharField(max_length=128 , default='')
    codigo_usuario = models.CharField(max_length=128, default='')
    contrasenia = models.CharField(max_length=128 , default='')


class tarea(models.Model):
    nombre_tarea = models.CharField(max_length=50,default='')
    descripcion = models.CharField(max_length=500, default='')
    fecha_de_creacion = models.DateField(default=datetime.date.today)
    fecha_entrega = models.DateField(default=datetime.date.today)
    usuario_responsable = models.CharField(max_length=128 , default='')
    estado_dela_tarea  =models.CharField(max_length=32 , default='PROGRESO')