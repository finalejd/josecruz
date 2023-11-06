from django.shortcuts import render, redirect
from .models import Equipos
from django.contrib import messages
from itertools import chain

# Create your views here.

def about(request):
    return render(request, "about_me.html")

def home(request):
    EquipoListado=Equipos.objects.all()
    messages.success(request, 'Team list')

    return render(request, "listadoEquipos.html", {"list": EquipoListado})
#---------------------------AGREGAR------------------------------#
def agregarEquipo(request):
    numEquipo=request.POST['numEquipo']
    nombreEquipo=request.POST['nombreEquipo']
    nombreCiudad=request.POST['nombreCiudad']
    nombreEstadio=request.POST['nombreEstadio']

    list=Equipos.objects.create(numEquipo=numEquipo, nombreEquipo=nombreEquipo, nombreCiudad=nombreCiudad, nombreEstadio=nombreEstadio)

    messages.success(request, 'Team added')
    return redirect('/')

#-----------------------------EDITAR-------------------------------#


#----------SELECCIONAR EDICION-----------#


def edicionEquipo(request, numEquipo):
    equipo=Equipos.objects.get(numEquipo=numEquipo)
    return render(request, "editarEquipo.html", {"list":equipo})


#----------EDITAR SELECCION-------------#
def editarEquipo(request): 
    numEquipo=request.POST['numEquipo']
    nombreEquipo=request.POST['nombreEquipo']
    nombreCiudad=request.POST['nombreCiudad']
    nombreEstadio=request.POST['nombreEstadio']

    equipo=Equipos.objects.get(numEquipo=numEquipo)
    equipo.nombreEquipo=nombreEquipo
    equipo.nombreCiudad=nombreCiudad
    equipo.nombreEstadio=nombreEstadio
    equipo.save()

    messages.success(request, 'Modified team')
    return redirect('/')


#---------------------------ELIMINAR EQUIPO------------------------------#

def eliminarEquipo(request, numEquipo):
    equipo=Equipos.objects.get(numEquipo=numEquipo)
    equipo.delete()

    messages.success(request, 'Team deleted')
    return redirect('/')

