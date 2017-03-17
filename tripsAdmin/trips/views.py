from django.shortcuts import render, get_object_or_404

from tripsAdmin.trips.models import Trip

def trips(request):
    trip = Trip.objects.all()
    context = {
        'trips': trip
    }
    return render(request, 'trips.html', context)

def details(request, slug):
    trip = get_object_or_404(Trip, slug=slug)
    context = {
        'trip':trip
    }
    return render(request, 'details.html', context)
