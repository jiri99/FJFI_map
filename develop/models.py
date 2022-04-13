from django.db import models


class Building(models.Model):
    name = models.TextField()
    address = models.TextField()
# Create your models here.


class Floor(models.Model):
    name = models.TextField()
    map = models.TextField()
# Create your models here.


class Room(models.Model):
    name = models.TextField()
    description = models.TextField()
# Create your models here.
