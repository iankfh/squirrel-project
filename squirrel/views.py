
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse

from .models import SquirrelSighting

def index(request):
    return HttpResponse("Index Page")

def map(request):
    return HttpResponse("Map")

def sightings(request):
    squirrel = SquirrelSighting.objects.all()
    context = {'squirrel': squirrel}
    return render(request, 'squirrel/all.html', context)

def squirrel_details(request):
    return HttpResponse("Squirrel details")

def add(request):
    return HttpResponse("Add")

def stats(request):
    return HttpResponse("Stats")

# Create your views here.
