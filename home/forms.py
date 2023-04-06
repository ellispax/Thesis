from django import forms
from django.contrib.auth.models import User
from .models import Farm

class FarmAddForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'crop', 'location', 'size', 'status']
        widgets = {            
            'status': forms.TextInput(attrs={'readonly': 'readonly'})
        }


class FarmToggleStatus(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'location', 'size', 'status']
        widgets = {
            'farm_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'location': forms.TextInput(attrs={'readonly': 'readonly'}),
            'size': forms.TextInput(attrs={'readonly': 'readonly'}),
        }