from django.conf.urls import url, include

from tripsAdmin.trips.views import trips

urlpatterns = [
    url(r'^$', trips, name="trips"),
]
