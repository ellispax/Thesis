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

    def __str__(self):
        return f'{self.farm}'