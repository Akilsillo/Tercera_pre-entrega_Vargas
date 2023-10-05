from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from FirstApp.forms import *
from FirstApp.models import *

# Create your views here.
def inicio(request):
    return render(request, "FirstApp/index.html")

def games(request):
    
    if request.method == "POST":
        
        miForm = GamesForm(request.POST)
        
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            # print(f"INFORMACION CLEANED: {informacion}")
            
            game = FinishedGames(name=informacion["name"], release_date=informacion["release_date"], rating=informacion["rating"])
            game.save()
            return render(request, "FirstApp/index.html")
    else:
        # print("CAMINO DEL GET")
        miForm = GamesForm()
        
    return render(request, "FirstApp/games.html", {"miForm": miForm})

def projectsToDo(request):
    
    if request.method == "POST":
        
        miForm = Projects(request.POST)
        
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            
            project = ProjectsToDo(name=informacion["name"], approx_time=informacion["approx_time"], description=informacion["description"])
            project.save()
            return render(request, "FirstApp/index.html")
    else:
        miForm = Projects()
        
    return render(request, "FirstApp/projects.html", {"miForm": miForm})

def hobbies(request):
    
    if request.method == "POST":
        
        miForm = HobbiesForm(request.POST)
        
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            
            hobbie = Hobbies(name=informacion["name"])
            hobbie.save()
            return render(request, "FirstApp/index.html")
    else:
        miForm = HobbiesForm()
        
    return render(request, "FirstApp/hobbies.html", {"miForm": miForm})

def searchGame(request):
    
    if request.method == "POST":
        
        miForm = SearchGame(request.POST)
        
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            
            games = FinishedGames.objects.filter(name__icontains=informacion["name"])
            
            return render(request, "FirstApp/search_result.html", {"games": games})
        
    else:
        miForm = SearchGame()
        
    return render(request, "FirstApp/search_game.html", {"miForm": miForm})