from django.urls import path
from .import views
from django.contrib import admin

urlpatterns=[
    path('', views.home),
    path('agregarEquipo/', views.agregarEquipo),
    path('edicionEquipo/<numEquipo>', views.edicionEquipo),
    path('editarEquipo/', views.editarEquipo),
    path('eliminarEquipo/<numEquipo>', views.eliminarEquipo),
    path('about/', views.about)

]

