from django.urls import path
from AppCoder import views

urlpatterns = [
    #path('curso/', curso), #esta es de la clase pasada 18

    path('inicioFull', views.inicioFull), #tengo todas las cosas de template
    path('', views.inicio, name="Inicio"), 
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('profesorVista', views.vistaProfesores, name="VistaProfesores"),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),

]

