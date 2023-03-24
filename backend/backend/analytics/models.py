from django.db import models
from home.models import Farm


# Create your models here.
class measurements(models.Model):
    farm= models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="an_farm_name", null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    temp = models.FloatField()
    pH = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()
    timeStamp = models.CharField(default = '2023101000000',max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.farm}'

class water_used(models.Model):
    farm= models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="wt_farm_name", null=True, blank=True)
    water_amnt = models.FloatField()
    date = models.DateField()
    t1 = models.TimeField()
    t2 = models.TimeField()
    