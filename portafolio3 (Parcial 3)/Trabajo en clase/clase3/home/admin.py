from django.contrib import admin
from .models import *

#Muestra los usuarios que estan registrados en la bd

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=[
        "user",
        "name",
        "email",
        "status"
    ]