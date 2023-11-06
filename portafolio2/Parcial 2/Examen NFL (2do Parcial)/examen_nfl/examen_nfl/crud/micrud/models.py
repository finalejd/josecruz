from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Equipos(models.Model):
    numEquipo=models.CharField(primary_key=True, max_length=10)
    nombreEquipo=models.CharField(max_length=50, blank=True, null=False)
    nombreCiudad=models.CharField(max_length=50, blank=True, null=True)
    nombreEstadio=models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombreEquipo, self.nombreCiudad)





    