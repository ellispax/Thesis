from django.db import models
from django.contrib.auth.models import User
from home.models import Farm


# Create your models here.

class Manage(models.Model):
    farm= models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="mg_farm_name", blank=True)
    temp = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()
    pH = models.FloatField()
    water = models.IntegerField()

    def __str__(self):
        return f'{self.farm}'