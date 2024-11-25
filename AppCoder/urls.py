from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio/',views.inicio,name='inicio' ),
    path('curso/',views.curso,name='curso' ),
    path('estudiante/',views.estudiante,name='estudiante' ),
    path('profesor/',views.profesor,name='profesor' ),
    path('entregable/',views.entregable,name='entregable' ),



    
]