from io import BytesIO

import requests
from django.core import files
from django.db import models

class LumberData(models.Model):
    Date = models.CharField(max_length=25, blank=True)
    Open = models.FloatField(max_length=25, blank=True)
    High = models.FloatField(max_length=25, blank=True)
    Low = models.FloatField(max_length=25, blank=True)
    Close = models.FloatField(max_length=25, blank=True)
    Volume = models.PositiveIntegerField(blank=True)
    Dividends = models.PositiveIntegerField(blank=True)
    Stock_Splits = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.Date

