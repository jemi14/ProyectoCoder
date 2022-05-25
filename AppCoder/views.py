

from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(request):

    curso = Curso(nombre="Excel", camada=54896)
    curso.save()
    
    documentoDeTexto = " "
    cursos = Curso.objects.all()

    for c in cursos: 

        documentoDeTexto =documentoDeTexto  +  f"---->Curso: {c.nombre} Camada: {c.camada} <br>"


    return HttpResponse(documentoDeTexto) #Http NO HTTP --- y poner from django.http import HttpResponse
