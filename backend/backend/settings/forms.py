from django import forms
from .models import Settings

class GeneralInfoForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = ['main_farm', 'template_name', 'farm_location', 'farm_contacts']
