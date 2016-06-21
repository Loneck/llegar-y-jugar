from django.db import models
from django.utils import timezone


# Create your models here.
class Recinto(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)

    def __str__(self):
        return '%s [%s]' % (self.nombre, self.id)


# class Cancha(models.Model):
#     nombre = models.CharField(max_length=200)
#     descripcion = models.CharField(max_length=200)
#     estado = models.BooleanField(default=True)
#     recinto = models.ForeignKey(Recinto, related_name='cancha_recinto')

#     def __str__(self):
#         return self.nombre


class Horario(models.Model):
    nombre = models.CharField(max_length=200)
    cancha = models.ManyToManyField(Cancha, through='Reserva')


class Reserva(models.Model):
    cancha = models.ForeignKey(Cancha, db_column='cancha')
    horario = models.ForeignKey(Horario, db_column='horario')
    fecha = models.DateTimeField()
