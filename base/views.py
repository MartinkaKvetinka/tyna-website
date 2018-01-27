from django.shortcuts import render
from .models import Content


def index(request):
    about_grainspace = Content.objects.get(name="about_grainspace")
    about_babysitting = Content.objects.get(name="about_babysitting")
    about_workshops = Content.objects.get(name="about_workshops")

    context = {"about_grainspace": about_grainspace,
               "about_babysitting": about_babysitting,
               "about_workshops": about_workshops}

    return render(request, 'base/index.html', context)


def about(request):
    about_me = Content.objects.get(name="about_me")
    context = {"about_me": about_me}
    return render(request, 'base/about.html', context)


def offer(request):
    return render(request, 'base/offer.html')


def grainspace(request):
    description_grainspace = Content.objects.get(name="description_grainspace")
    context = {"description_grainspace": description_grainspace}
    return render(request, 'base/grainspace.html', context)


def babysitting(request):
    description_babysitting = Content.objects.get(name="description_babysitting")
    context = {"description_babysitting": description_babysitting}
    return render(request, 'base/babysitting.html', context)


def workshops(request):
    description_workshops = Content.objects.get(name="description_workshops")
    context = {"description_workshops": description_workshops}
    return render(request, 'base/workshops.html', context)


def timetable(request):
    return render(request, 'base/timetable.html')


def contact(request):
    return render(request, 'base/contact.html')
