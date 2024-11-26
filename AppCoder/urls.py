from django.urls import path
from AppCoder import views
from .views import lista_docente, lista_alumno , lista_universidad , lista_envio, buscar_universidades

urlpatterns = [
    path('inicio/',views.inicio,name='inicio' ),

    # BUSQUEDA DE UNIVERSIDADES FORMULARIO GET

    path('buscar_universidades/', buscar_universidades, name='buscar_universidades'),

    # AGREGAR FORMULARIOS POST
    path('agregar_universidad/',views.agregar_universidad,name='agregar_universidad' ),
    path('agregar_alumno/',views.agregar_alumno,name='agregar_alumno' ),
    path('agregar_docente/',views.agregar_docente,name='agregar_docente' ),
    path('agregar_envio/',views.agregar_envio,name='agregar_envio' ),
    
    # URLs DE TODAS LAS LISTAS
    path('lista_docente/', lista_docente, name='lista_docente'),
    path('lista_alumno/', lista_alumno, name='lista_alumno'),
    path('lista_universidad/', lista_universidad, name='lista_universidad'),
    path('lista_envio/', lista_envio, name='lista_envio'),


]