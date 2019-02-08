from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre=models.CharField(max_length=100)
    fundacion=models.IntegerField()
    estadio=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.IntegerField()
    posicion=models.CharField(max_length=100)
    equipo=models.ForeignKey(Equipo, on_delete=models.CASCADE)

class Estadio(models.Model):
    nombre=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)
    capacidad=models.IntegerField()
    equipo=models.CharField(max_length=100)