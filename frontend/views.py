from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Building

# Create your views here.
def home_view(request, *args, **kwargs):
    queryset = Building.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "frontend/home.html", context)