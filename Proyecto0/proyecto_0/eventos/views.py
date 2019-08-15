from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.shortcuts import render, get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone



from .models import Evento
import datetime


# Create your views here.
@csrf_exempt
def agregarUsuarioview(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        usuario = jsonUser['username']
        contrasena = jsonUser['password']

        user_model=User.objects.create_user(username=usuario, password= contrasena, last_login=timezone.now())
        #user_model.last_login = timezone.now() update_fields=['last_login']
        user_model.save()

    return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def agregarUsuario(request):
    return render(request, "eventos/registro.html")


@csrf_exempt
def index(request):
    if request.user.is_authenticated:
        eventos_list = Evento.objects.filter(user=request.user).order_by('-id')
    else:
        eventos_list = ""
    return render(request, "eventos/index.html", {'eventos':eventos_list})


@csrf_exempt
def agregarEvento(request):
    if request.method == 'POST':
        newEvento = Evento(
            nombre=request.POST.get('nombre'),
            categoria=request.POST.get('categoria'),
            lugar=request.POST.get('lugar'),
            direccion=request.POST.get('direccion'),
            fecha_ini=datetime.datetime.strptime(request.POST.get('fecha_ini'),'%Y-%m-%d'),
            fecha_fin=datetime.datetime.strptime(request.POST.get('fecha_fin'),'%Y-%m-%d'),
            tipo=request.POST.get('tipo'),
            user=request.user)
        newEvento.save()

    return HttpResponse(serializers.serialize("json", [newEvento]))


@csrf_exempt
def agregarNuevoEvento(request):
    return render(request, "eventos/evento_form.html")


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        password = jsonUser['password']
        email = jsonUser['username']
        user=authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            message="ok"
        else:
            message='El e-mail o la contraseña son inconrrectos'

    return JsonResponse({"message":message})


@csrf_exempt
def login_user(request):
    return render(request, "eventos/login.html")


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message":'ok'})


@csrf_exempt
def is_logged_view(request):
    if request.user.is_authenticated:
        message = 'ok'
    else:
        message = 'no'
    return JsonResponse({"message": message})


@csrf_exempt
def verDetalle(request,pk):
    evento=Evento.objects.filter(id=pk)[0]
    return render(request, 'eventos/detalle.html',{'evento':evento})

@csrf_exempt
def eliminarEvento(request,pk):
    evento=Evento.objects.filter(id=pk)
    evento.delete()
    return HttpResponseRedirect('/eventos/')

@csrf_exempt
def editarEventoView(request,pk):
    evento=Evento.objects.filter(id=pk)[0]
    if request.method == 'POST':
        evento.nombre=request.POST.get('nombre')
        evento.categoria=request.POST.get('categoria')
        evento.lugar=request.POST.get('lugar')
        evento.direccion=request.POST.get('direccion')
        evento.fecha_ini=datetime.datetime.strptime(request.POST.get('fecha_ini'),'%Y-%m-%d')
        evento.fecha_fin=datetime.datetime.strptime(request.POST.get('fecha_fin'),'%Y-%m-%d')
        evento.tipo=request.POST.get('tipo')
        evento.save()
    return HttpResponse(serializers.serialize("json", [evento]))

@csrf_exempt
def editarEvento(request,pk):
    evento = Evento.objects.filter(id=pk)[0]
    return render(request, "eventos/evento_form2.html",{'evento':evento})




