from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from crops.models import Crops
# Create your models here.


class Farm(models.Model):
    farm_name = models.CharField(max_length=150)
    crop = models.ForeignKey(Crops,on_delete=models.CASCADE, related_name='cult_crop')
    location = models.CharField(max_length=20)
    size = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.farm_name}'


class Notifications(models.Model):
    farm= models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="n_farm_name")
    notification = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    notified = models.BooleanField(default=False) 