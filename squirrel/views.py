
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import SquirrelSighting
from .forms import SightingForm

def index(request):
    return HttpResponse("Index Page")

def map(request):
    sightings = SquirrelSighting.objects.all()[:100]
    context = {'sightings': sightings}
    return render(request, 'squirrel/map.html', context)

def sightings(request):
    squirrel = SquirrelSighting.objects.all()
    context = {'squirrel': squirrel}
    return render(request, 'squirrel/all.html', context)

def detail(request, unique_squirrel_id):
    squirrel = get_object_or_404(SquirrelSighting, unique_squirrel_id=unique_squirrel_id)
    form = SightingForm(request.POST or None, instance=squirrel)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('squirrel:sightings'))
    return render(request, 'squirrel/detail.html', {'form': form})

def add(request):
    if request.method=='Post':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('squirrel:sightings'))
        else:
            form = SightingForm()
            context = {'form':form}
            return render(request, 'sightings/add.html', context)


def stats(request):
    return HttpResponse("Stats")


