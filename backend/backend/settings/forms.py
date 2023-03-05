from django import forms
from .models import Settings
from home.models import Farm
from crops.models import Crops

class GeneralInfoForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = ['main_farm', 'template_name', 'farm_location', 'farm_contacts']


class UpdateFarmForm(forms.ModelForm):
	class Meta:
		model = Farm
		fields = ['farm_name', 'crop', 'location', 'size']


class AddCropForm(forms.ModelForm):
	class Meta:

		model = Crops
		fields = ['cropName', 'region', 'temp', 'pH', 'humidity', 'moisture', 'water_needed']

class UpdateCropForm(forms.ModelForm):
	class Meta:
		model = Crops
		fields = ['cropName', 'region', 'temp', 'pH', 'humidity', 'moisture', 'water_needed']
		widgets = {
            'cropName': forms.TextInput(attrs={'readonly': 'readonly'}),
            
        }

