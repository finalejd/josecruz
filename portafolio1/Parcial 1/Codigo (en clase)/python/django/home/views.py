


from django.shortcuts import render
from .models import Mascota
# Create your views here.

def index2(request):
    return render(request,"home/index2.html",{})
def index3 (request):
    return render(request,"home/index3.hmtl",{})

def index4 (request):
   return render(request,"base/base.html", {})
#
#class DetailCategory(generic.DetailVew):
        #template_name= 

def index(request):
    datosMascota=Mascota.objects.all()
    return render(request,"home/index.html",{"mascotas":datosMascota})
   
