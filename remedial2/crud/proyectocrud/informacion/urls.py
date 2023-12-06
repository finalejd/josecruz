from django.urls import path
from . import views

urlpatterns = [

#MENU
    path('', views.base),
    path('menuPlayer/', views.menuPlayer),
    path('menuStadium/', views.menuStadium),
    path('menuTeams/', views.menuTeams),
    
#PLAYER
    path('registerPlayer/', views.registerPlayer),
    path('editionPlayer/<number>', views.editionPlayer),
    path('editPlayer/', views.editPlayer),
    path('deletePlayer/<number>', views.deletePlayer),

#TEAMS
    path('registerTeams/', views.registerTeams),
    path('editionTeams/<number>', views.editionTeams),
    path('editTeams/', views.editTeams),
    path('deleteTeams/<number>', views.deleteTeams),

#STADIUIM
    path('registerStadium/', views.registerStadium),
    path('editionStadium/<number>', views.editionStadium),
    path('editStadium/', views.editStadium),
    path('deleteStadium/<number>', views.deleteStadium),
    
]