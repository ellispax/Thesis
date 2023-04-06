
from django.db import models
from django.contrib.auth.models import User
from home.models import Farm

# Create your models here.

class Transaction(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="tr_farm_name", null=True, blank=True)
    action_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="logs_user")
    action = models.BooleanField()
    action_date = models.DateField()
    action_time = models.TimeField()
