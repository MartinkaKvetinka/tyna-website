from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    # /
    path('', views.index, name="index"),
    # /about
    path('about/', views.about, name="about"),
    # /offer
    path('offer/', views.offer, name="offer"),
    # /grainspace
    path('grainspace/', views.grainspace, name="grainspace"),
    # /babysitting
    path('babysitting/', views.babysitting, name="babysitting"),
    # /workshops
    path('workshops/', views.workshops, name="workshops"),
    # /timetable
    path('timetable/', views.timetable, name="timetable"),
    # /inspiration
    path('inspiration/', views.inspiration, name="inspiration"),
    # /contact
    path('contact/', views.contact, name="contact"),
]
