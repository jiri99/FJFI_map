from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from collections import OrderedDict
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
    return render(request, "develop/home.html", context)

def homepage_view(request, *args, **kwargs):
    queryset = Building.objects.all()
    context = {
        "object_building": queryset
    }
    return render(request, "develop/homepage.html", context)

def navbar_view(request, *args, **kwargs):
    queryset = Building.objects.all()
    queryset_size =[{"size": 756, "color": "#AAD1FF"},
                    {"size": 648, "color": "#93C4FF"},
                    {"size": 540, "color": "#80BAFF"},
                    {"size": 432, "color": "#6FB0FF"}, 
                    {"size": 324, "color": "#5DA6FD"}, 
                    {"size": 216, "color": "#4E9DFA"}, 
                    {"size": 108, "color": "#4886FF"}, 
                    {"size": 0, "color": "#4870FF"}]
    context = {
        "object_building": queryset,
        "ellipse_style": queryset_size
    }
    return render(request, "develop/navbar.html", context)

def display_view(request, *args, **kwargs):
    queryset_room = Room.objects.all().order_by('id')
    queryset_floor = Floor.objects.all().order_by('id')
    queryset_building = Building.objects.all()
    context = {
        "object_floor": queryset_floor,
        "object_building": queryset_building,
        "object_room": queryset_room
    }
    return render(request, "develop/display.html", context)

def classes_view(request, *args, **kwargs):
    queryset = Room.objects.filter(room_type__id = 2)
    context = {
        "rooms": queryset
    }
    return render(request, "develop/classes.html", context)

def important_view(request, *args, **kwargs):
    queryset = Room.objects.filter(room_type__id = 4)
    context = {
        "rooms": queryset
    }
    return render(request, "develop/important.html", context)

def wc_view(request, *args, **kwargs):
    queryset = Room.objects.filter(room_type__id = 5)
    context = {
        "rooms": queryset
    }
    return render(request, "develop/wc.html", context)

def others_view(request, *args, **kwargs):
    queryset = Room.objects.filter(room_type__id = 6)
    context = {
        "rooms": queryset
    }
    return render(request, "develop/others.html", context)

def favourite_view(request, *args, **kwargs):
    context = {}
    return render(request, "develop/favourite.html", context)

def search_view(request, *args, **kwargs):
    results = []
    searched = []
    if request.method == "POST":
        searched = request.POST['search']
        # if searched == '':
        #     searched = 'None'
        # else:
        results = Room.objects.filter(name__contains=searched)
    return render(request, 'develop/search.html', {'searched': searched, 'results': results})

def room_search_view(request, *args, **kwargs):
    results = Room.objects.all()
    return render(request, 'develop/room_search.html', {'rooms': results})

def room_view(request, room_id):
    print(room_id)
    room = Room.objects.get(pk=room_id)
    # floors = Floor.objects.all()
    # floor = floors.get(id=room.floor.id)
    return render(request, 'develop/room_detail.html', {'room': room})
    # return render(request, 'develop/room_detail.html', {'room': room, 'name': floor.name})