from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


class Farmer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Culture(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.PolygonField(srid=4326)
    objects = models.Manager()
    farmer = models.ForeignKey(Farmer, null=True,  on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, null=True, on_delete=models.CASCADE)
    seasons = models.ForeignKey(Season, null=True, on_delete=models.CASCADE)

