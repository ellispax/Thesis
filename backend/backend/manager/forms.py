from django import forms
from .models import Manage

class ManageUpdateForm(forms.ModelForm):
    class Meta:
        model = Manage
        fields = ['farm','temp','humidity','moisture', 'pH', 'water']
        widgets = {
            'farm': forms.TextInput(attrs={'readonly': 'readonly'}),
            
            
        }