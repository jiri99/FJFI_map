from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.append('../')
from develop.models import Building, Floor, Room
# from .models import Building

# Create your views here.
def home_view(request, *args, **kwargs):
    queryset = Building.objects.all()
    context = {
        "name": queryset
    }
    return render(request, "frontend/home.html", context)

def homepage_view(request, *args, **kwargs):
    queryset = Building.objects.all()
    context = {
        "object_building": queryset
    }
    return render(request, "frontend/homepage.html", context)

def display_view(request, *args, **kwargs):
    queryset = Floor.objects.all()
    context = {
        "object_floor": queryset
    }
    return render(request, "frontend/display.html", context)

def classes_view(request, *args, **kwargs):
    queryset = Room.objects.filter(room_type__id = 2)
    context = {
        "rooms": queryset
    }
    return render(request, "frontend/classes.html", context)

def important_view(request, *args, **kwargs):
    queryset = Room.objects.filter(room_type__id = 4)
    context = {
        "rooms": queryset
    }
    return render(request, "frontend/important.html", context)

def wc_view(request, *args, **kwargs):
    queryset = Room.objects.filter(room_type__id = 5)
    context = {
        "rooms": queryset
    }
    return render(request, "frontend/wc.html", context)

def others_view(request, *args, **kwargs):
    queryset = Room.objects.filter(room_type__id = 6)
    context = {
        "rooms": queryset
    }
    return render(request, "frontend/others.html", context)