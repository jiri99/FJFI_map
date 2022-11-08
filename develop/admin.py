from django.contrib import admin
from .models import Building, Floor, Room, Room_type

admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Room_type)

# Register your models here.
