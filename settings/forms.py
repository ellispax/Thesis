from django import forms
from .models import Settings
from home.models import Farm
from crops.models import Crops
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

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
		fields = ['cropName', 'region', 'temp', 'ph_min','ph_max', 'humidity', 'moisture']

class UpdateCropForm(forms.ModelForm):
	class Meta:
		model = Crops
		fields = ['cropName', 'region', 'temp', 'ph_min','ph_max', 'humidity', 'moisture']
		widgets = {
            'cropName': forms.TextInput(attrs={'readonly': 'readonly'}),
            
        }

