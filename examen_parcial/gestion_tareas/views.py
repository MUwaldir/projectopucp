from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from gestion_tareas.models import usuario,tarea
from dateutil.parser import parse
from datetime import *
# Create your views here.

def login(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('itemUsuario')
        passwordUsuario = request.POST.get('itemPassword')
        usuario_registrado = 0
        usuarios_totales = usuario.objects.all()
        for user in usuarios_totales:
            if nombreUsuario == user.nombre and passwordUsuario == user.contrasenia:
                usuario_registrado = 1

        if usuario_registrado == 1 :
            
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
        else:
            return render(request, 'gestion_tareas/login.html',{
                'mensaje' : 'Los datos ingresados no son correctos'})
   
    return render(request, 'gestion_tareas/login.html')


def dashboard(request):
    hoy =date.today()
    tareas_totales = tarea.objects.all()
    tarea_user= tarea.objects.filter(usuario_responsable = 'waldir' )
    for tareas in tarea_user:
        if tareas.estado_dela_tarea != 'FINALIZADO':
            dif = tareas.fecha_entrega - date.today()
            if dif.days <= 2 and dif.days >= 0:
                tareas.estado_dela_tarea = 'FINALIZANDO' 
                tareas.save()
            elif dif.days < 0:
                tareas.estado_dela_tarea = 'PENDIENTE'
                tareas.save()
            elif dif.days > 2 :
                tarea.estado_dela_tarea = 'PROGRESO'
                tareas.save()
    return render(request, 'gestion_tareas/dashboard.html',{'tareas_usuario': tarea_user, 'hoy':hoy})

def crear(request):
    fecha =date.today()
    if request.method == 'POST':
        responsable = request.POST.get('usuario_res')
        fechainicio = request.POST.get('fechainicio')
        fechainicio = parse(fechainicio)
        fechaentrega = request.POST.get('fechaentrega')
        fechaentrega = parse(fechaentrega)
        descripcion = request.POST.get('description')
        tarea(usuario_responsable = responsable,descripcion= descripcion, fecha_de_creacion=fechainicio, fecha_entrega=fechaentrega).save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request, 'gestion_tareas/vista_creacion.html',{'fecha': fecha})

def editar(request, tareas_id):
        tarea_info = tarea.objects.get(id = tareas_id)
        if request.method == 'POST':
            responsable = request.POST.get('usuario_res')
            fechainicio = request.POST.get('fechainicio')
            fechainicio = parse(fechainicio)
            fechaentrega = request.POST.get('fechaentrega')
            fechaentrega = parse(fechaentrega)
            descripcion = request.POST.get('description')
            tarea_info.usuario_responsable = responsable
            tarea_info.fecha_de_creacion = fechainicio
            tarea_info.fecha_entrega = fechaentrega
            tarea_info.descripcion = descripcion
            tarea_info.estado_dela_tarea = 'PROGRESO'
            tarea_info.save()
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
            
        return render(request, 'gestion_tareas/vista_edicion.html',{'tareas_editar':tarea_info})

def delete(request, tareas_id):
    tarea_info = tarea.objects.get(pk = tareas_id)
    tarea_info.delete()
    return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))

def detalle(request,tareas_id):
    tareas_info = tarea.objects.get(id = tareas_id)
    if request.method == 'POST':
        tareas_info.estado_dela_tarea = 'FINALIZADO'
        tareas_info.save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request, 'gestion_tareas/vista_detallada.html',{'tarea_detalle': tareas_info})

