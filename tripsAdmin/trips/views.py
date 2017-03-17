from django.shortcuts import render

from tripsAdmin.trips.models import Trip

def trips(request):
    trip = Trip.objects.all()
    context = {
        "trips": trip
    }
    return render(request, 'trips.html', context)
