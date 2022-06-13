from django.urls import path
from AppCoder import views

#---------------Clase 23-------------------------------
from django.contrib.auth.views import LogoutView

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
    path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name='EditarProfesor'),

    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),

#---------------Clase 23-------------------------------
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),

#---------------Clase 24-------------------------------
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar")

]

