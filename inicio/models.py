from django.db import models

# Create your models here.


class Inicio(models.Model):
	idInicio = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=200)
	
