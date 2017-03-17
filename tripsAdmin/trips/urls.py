from django.conf.urls import url, include

from tripsAdmin.trips.views import trips, details

urlpatterns = [
    url(r'^$', trips, name="trips"),
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
]
