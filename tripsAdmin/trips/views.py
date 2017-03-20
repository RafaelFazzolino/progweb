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

def search(request):
    if request.method == 'GET':
        search = request.GET['search']
        trip = get_object_or_404(Trip, title__icontains=search)
        context = {
            'trip': trip,
            'search': search
        }
        return render(request, 'details.html', context)
    else:
        return render(request, 'home.html')
