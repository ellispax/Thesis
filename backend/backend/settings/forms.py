from django import forms
from .models import Settings
from home.models import Farm
class GeneralInfoForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = ['main_farm', 'template_name', 'farm_location', 'farm_contacts']


class UpdateFarmForm(forms.ModelForm):
	class Meta:
		model = Farm
		fields = ['farm_name', 'location', 'size']
