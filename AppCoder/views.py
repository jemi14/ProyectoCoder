from django.http import HttpResponse
from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso
from django.shortcuts import render
from AppCoder.forms import ProfesorFormulario
from AppCoder.models import Profesor
from django.template import loader

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

#---------------Clase 21-------------------------------

def cursos(request):
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST) #Aquí me llega todo la info del html

        print(miFormulario)

        if miFormulario.is_valid: #Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html") #podes volver a donde quieras, si vuelve 
                                                           #al inicio es por que salio todo bien :)
    else:
        miFormulario= CursoFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def profesores(resquest):
    return render(resquest, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

#---------------Clase 20-------------------------------

def inicioFull(request):
    return render(request, "AppCoder/inicioFull.html")

#---------------Clase 21-------------------------------

def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST) #Aquí me llega todo la info del html

        print(miFormulario)

        if miFormulario.is_valid: #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])
            
            curso.save()
            
            return render(request, "AppCoder/inicio.html") #podes volver a donde quieras, si vuelve 
                                                           #al inicio es por que salio todo bien :)

    else:
        miFormulario= CursoFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})


def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST) #aqui me llega toda la info del html
        print(miFormulario)
        if miFormulario.is_valid: #Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'], profesion=informacion['profesion'])

            profesor.save()

            return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
    else:
        miFormulario=ProfesorFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})


#------Crear vista profesor----------

def vistaProfesores(request):

    #Trae todos los profesores de la base de datos
    listaDeProfesores = Profesor.objects.all()

    #cambiar en settigns DIRs (en el proyecto y poner): "C:/Users/grise/Desktop/Python/Clase18/Nuestro Primer MVT/Desafio18/AppDesafio18/plantillas/AppDesafio18
    #crear el html
    #importar from django.template import loader
    #Crear el diccionario con la info, cargar la plantilla con loader, generar el documento y enviarlo con http

    diccionario = {"listaDeProfesores":listaDeProfesores}  
    plantilla=loader.get_template("vistaDeProfesores.html")
    documento=plantilla.render(diccionario)
        
    return HttpResponse(documento)

#------Busqueda con form-------------

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos":cursos, "camada":camada})

    else:
        respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)