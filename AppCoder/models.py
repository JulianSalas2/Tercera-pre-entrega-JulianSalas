from django.db import models

# Create your models here.

class Curso(models.Model):
    Nombre = models.CharField(max_length= 30)
    Camada = models.IntegerField()