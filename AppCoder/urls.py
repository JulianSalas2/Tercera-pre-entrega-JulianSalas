from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio/',views.inicio,name='inicio' ),
    path('universidad/',views.Universidad,name='universidad' ),
    path('alumno/',views.Alumno,name='alumno' ),
    path('docente/',views.Docente,name='docente' ),
    path('envio/',views.Envio,name='envio' ),



    
]