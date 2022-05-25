from django.urls import path
from AppCoder import views

urlpatterns = [
    #path('curso/', curso), #esta es de la clase pasada 18

    path('', views.inicio), 
    path('cursos', views.cursos, name="Cursos"), #esta es la clase 19, name es para usarlo en el html
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
]

