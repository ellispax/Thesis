from django.db import models

# Create your models here.
class Crops(models.Model):
    cropName = models.CharField(max_length=20)
    region = models.CharField(max_length=25)
    temp = models.FloatField()
    pH = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()
    water_needed = models.FloatField()

    def __str__(self):
        return f'{self.cropName}'
