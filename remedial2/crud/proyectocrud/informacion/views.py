from django.shortcuts import render,redirect
from .models import Teams,Player, Stadium

# Create your views here.

#######################MENU MODELS & BASE#################################

def menuTeams(request):
    ListTeams = Teams.objects.all()
    ListStadium = Stadium.objects.all()
    return render (request, "menuteams.html", {"teams": ListTeams, "stadiums": ListStadium})

def menuPlayer(request):
    ListPlayer = Player.objects.all()
    ListTeams = Teams.objects.all()
    return render (request, "menuplayer.html", {"players": ListPlayer, "teams": ListTeams})

def menuStadium(request):
    ListStadium = Stadium.objects.all()
    return render (request, "menustadium.html", {"stadiums": ListStadium})

def base(request):
    return render (request, "base.html")

######################################################################

#######################FUNCTIONS TEAMS#################################


def registerTeams(request): 
    number = request.POST['number']
    nameTeam = request.POST['nameTeam']
    venue = request.POST['venue']
    ownerName = request.POST['ownerName']


    teams = Teams.objects.create(number=number, nameTeam=nameTeam, venue=venue, ownerName=ownerName)
    return redirect('/menuTeams/')

def editionTeams(request, number):
    teams = Teams.objects.get(number=number)
    return render(request, "editteam.html", {"teams": teams})

def editTeams(request):
    number = request.POST['number']
    nameTeam = request.POST['nameTeam']
    venue = request.POST['venue']
    ownerName = request.POST['ownerName']
    stadium = request.POST['stadium']


    teams = Teams.objects.get(number=number)
    teams.nameTeam = nameTeam
    teams.venue = venue
    teams.ownerName = ownerName
    teams.stadium = stadium
    teams.save()
    return redirect('/menuTeams/')

def deleteTeams(request, number):
    teams = Teams.objects.get(number=number)
    teams.delete()

    return redirect('/menuTeams/')

######################################################################

#######################FUNCTIONS PLAYER#################################


def registerPlayer(request): 
    number = request.POST['number']
    namePlayer = request.POST['namePlayer']
    playerNumber = request.POST['playerNumber']
    playerPosition = request.POST['playerPosition']

    player = Player.objects.create(number=number, namePlayer=namePlayer, playerNumber=playerNumber, playerPosition=playerPosition)
    return redirect('/menuPlayer/')

def editionPlayer(request, number):
    player = Player.objects.get(number=number)
    return render(request, "editplayer.html", {"player": player})

def editPlayer(request):
    number = request.POST['number']
    namePlayer = request.POST['namePlayer']
    playerNumber = request.POST['playerNumber']
    playerPosition = request.POST['playerPosition']

    player = Player.objects.get(number=number)
    player.namePlayer = namePlayer
    player.playerNumber = playerNumber
    player.playerPosition = playerPosition
    player.save()
    return redirect('/menuPlayer/')

def deletePlayer(request, number):
    player = Player.objects.get(number=number)
    player.delete()

    return redirect('/menuPlayer/')

######################################################################

#######################FUNCTIONS STADIUM#################################

def registerStadium(request): 
    number = request.POST['number']
    nameStadium = request.POST['nameStadium']
    capacity = request.POST['capacity']
    boxSize = request.POST['boxSize']

    stadium = Stadium.objects.create(number=number, nameStadium=nameStadium, capacity=capacity, boxSize=boxSize)
    return redirect('/menuStadium/')

def editionStadium(request, number):
    stadium = Stadium.objects.get(number=number)
    return render(request, "editstadium.html", {"stadium": stadium})

def editStadium(request):
    number = request.POST['number']
    nameStadium = request.POST['nameStadium']
    capacity = request.POST['capacity']
    boxSize = request.POST['boxSize']

    stadium = Stadium.objects.get(number=number)
    stadium.nameStadium = nameStadium
    stadium.capacity = capacity
    stadium.boxSize = boxSize
    stadium.save()
    return redirect('/menuStadium/')

def deleteStadium(request, number):
    stadium = Stadium.objects.get(number=number)
    stadium.delete()

    return redirect('/menuStadium/')





