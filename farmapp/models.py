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
    # plot = models.CharField(max_length=50, null=True)
    name = models.PolygonField(srid=4326)
    plot = models.CharField(max_length=50, null=True, verbose_name='Поле')
    objects = models.Manager()
    farmer = models.ForeignKey(Farmer, null=True,  on_delete=models.CASCADE, verbose_name='Фермер')
    culture = models.ForeignKey(Culture, null=True, on_delete=models.CASCADE, verbose_name='Культура')
    seasons = models.ForeignKey(Season, null=True, on_delete=models.CASCADE, verbose_name='Сезон')

    def __str__(self):
        return self.plot

    class Meta:
        verbose_name_plural = 'Поля'
        verbose_name = 'Поле'

