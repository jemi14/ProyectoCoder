from django.http import HttpResponse
from AppCoder.models import Curso
from django.shortcuts import render

# Create your views here.

def curso(request):

    curso = Curso(nombre="Excel", camada=54896)
    curso.save()
    
    documentoDeTexto = " "
    cursos = Curso.objects.all()

    for c in cursos: 

        documentoDeTexto =documentoDeTexto  +  f"---->Curso: {c.nombre} Camada: {c.camada} <br>"


    return HttpResponse(documentoDeTexto) #Http NO HTTP --- y poner from django.http import HttpResponse

#---------------Clase 19-------------------------------

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(resquest):
    return render(resquest, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

#---------------Clase 20-------------------------------

def inicioFull(request):
    return render(request, "AppCoder/inicioFull.html")