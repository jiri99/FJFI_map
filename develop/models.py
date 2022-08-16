from django.db import models


class Building(models.Model):
    name = models.TextField()
    address = models.TextField()

    def building_get_all_rooms():
        print("Hello world!")

    def building_get_all_floors():
        print("Hello world!")

    def find_wc():
        print("Hello world!")


class Floor(models.Model):
    building = models.ForeignKey(
        Building,
        on_delete=models.PROTECT,
        verbose_name=('building'),
        related_name='floor_in_building'
    )
    name = models.TextField()
    caption = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='develop/db_images')

    def floor_get_all_rooms():
        print("Hello world!")    

class Room(models.Model):
    floor = models.ForeignKey(
        Floor,
        on_delete=models.PROTECT,
        verbose_name=('floor'),
        related_name='room_on_floor'
    )
    name = models.TextField()
    description = models.TextField()
