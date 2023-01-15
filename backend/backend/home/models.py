from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Farm(models.Model):
    farm_name = models.CharField(max_length=150)
    location = models.CharField(max_length=20)
    size = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.farm_name}'

    # def get_company_rates(self):
    #     return Company_rates.objects.filter(company=self).first()