from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout, login, authenticate
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import *
from. forms import forms, User


# Create your views here.

#class Index(generic.View):
 #   template_name = "home/index.html"
  #  context = {}

  ###
   ##    return render(request, self.template_name, self.context)


class About(generic.View):
    template_name = "home/about.html"
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class Contact(generic.View):
    template_name = "home/contact.html"
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    

 # create user authenticate login/logout

class Index(generic.View):
    template_name ="home/index.html"
    context={}
    form=LoginForm()

    def get(self, request):
        self.context={
            "form": self.form
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        username= request.POST["username"]
        password= request.POST["password"]
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')

    
class Logout(generic.View):
    def get(self, request):
        logout(request)
        return redirect('/')
    
# Clase de inicio de sesion#

class SignUp(generic.CreateView):
    template_name="home/signup.html"
    model= User
    form_class = UserForm
    success_url= reverse_lazy("home:signup")

    def form_valid(self, form):
        form.save()  #se guarda primero los datos en la base de datos
        username=form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password1)
        if user is not None:
            login(self.request, user)
        id = form.cleaned_data.get("id")
        print(id)
        return redirect("home:index")

# Viesw para que el usuario visualice su profile
class DetailProfile(generic.View):
    template_name="home/detail_profile.html"
    context={}

    def get(self, request, pk):
        self.context = {
            "profile": Profile.objects.get(id=pk)
            
        }
        return render(request, self.template_name, self.context) 
    


