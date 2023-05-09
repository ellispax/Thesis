from django import forms
from .models import Manage

class ManageUpdateForm(forms.ModelForm):
    class Meta:
        model = Manage
        fields = ['farm','temp','humidity','moisture', 'ph_min', 'ph_max']
        widgets = {
            'farm': forms.TextInput(attrs={'readonly': 'readonly'}),
            
            
        }