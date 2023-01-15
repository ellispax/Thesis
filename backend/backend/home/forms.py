from django import forms
from django.contrib.auth.models import User
from .models import Farm

class FarmAddForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'location', 'size', 'status']