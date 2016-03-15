from django.db import models
from recinto.models import Recinto


class Cancha(models.Model):
	idRecinto = models.ForeignKey(Recinto)
	idCancha = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=200)
	latitud = models.CharField(max_length=200)
	estado = models.BooleanField(default='False')
# Create your models here.
