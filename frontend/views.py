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
    queryset = Floor.objects.get(id=1)
    context = {
        "object_floor": queryset
    }
    print(context["object_floor"].image)
    return render(request, "frontend/display.html", context)