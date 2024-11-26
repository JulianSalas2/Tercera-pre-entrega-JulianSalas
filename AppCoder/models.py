from django.db import models

# Create your models here.

class Universidad(models.Model):
    nombre = models.CharField(max_length= 30)
    pais= models.CharField(max_length=30)
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    id_estudiante = models.IntegerField()

class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Envio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField() 
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()       

