from django.db import models
# Create your models here.


class Settings(models.Model):
    main_farm = models.CharField(default="farm", max_length=255)
    template_name = models.CharField(default="Farm Inc.", max_length=255)
    farm_location= models.CharField(default="Farm Location", max_length=255)
    farm_contacts = models.CharField(default="02 xxx-xxxx / 02 xxx-xxxx", max_length=255)
   
    def __str__(self):
        return f'{self.main_farm}'


# class BracketSSContribEE(models.Model):
# 	contrib_amount = models.DecimalField(max_digits=7, decimal_places=2, null=True)
# 	ranged = models.CharField(max_length=100)
