from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Settings
from .forms import GeneralInfoForm
from django.contrib import messages
from home.models import Farm
from crops.models import Crops
from home.forms import FarmAddForm
from .forms import UpdateFarmForm , AddCropForm , UpdateCropForm
from django.contrib.auth.decorators import login_required

@login_required
def update_show(request):
    farms = Farm.objects.all()
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_farm'] = gen_settings.main_farm
    else:
        request.session['main_farm'] = ""
    # return render(request, 'hrms/dashboard.html', context)

    context = {
        'title': 'Update Farm Details',
        'head': 'Settings',
        'farms': farms
    }
    return render(request, 'settings/all_farms.html', context)


def show_crops(request):
    crops = Crops.objects.all()
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_farm'] = gen_settings.main_farm
    else:
        request.session['main_farm'] = ""
    # return render(request, 'hrms/dashboard.html', context)

    context = {
        'title': 'Udate Crop Details',
        'head': 'Crop-Settings',
        'crops': crops
    }
    return render(request, 'settings/crops.html', context)


@login_required
def update_farm(request, pk):
    farm = get_object_or_404(Farm, id=pk)
    
    if request.method == 'POST':
        
        form = UpdateFarmForm(request.POST or None, instance=farm)
        
        if form.is_valid():
            form.save()
            #action = ""
            # Transaction.objects.create(action=action, action_by=request.user, farm_id = pk, action_date=datetime.now(),action_time=timezone.now())
            messages.success(request, f'Farm Details were successfully updated.')
            return redirect('update-show')
    else:
        # form = FarmAddForm(instance=farm)
        form = UpdateFarmForm(instance=farm)


    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'head': 'Update Farm Details',
        'page_nick': 'cr-update',
        'form': form,
        'farm_id': pk
    }
    return render(request, 'settings/update_farm.html', context)

@login_required
def update_crop(request, pk):
    crop = get_object_or_404(Crops, id=pk)
    
    if request.method == 'POST':
        
        form = UpdateCropForm(request.POST or None, instance=crop)
        
        if form.is_valid():
            form.save()
            #action = ""
            # Transaction.objects.create(action=action, action_by=request.user, farm_id = pk, action_date=datetime.now(),action_time=timezone.now())
            messages.success(request, f'Crop Details were successfully updated.')
            return redirect('show-crops')
    else:
        # form = FarmAddForm(instance=farm)
        form = UpdateCropForm(instance=crop)


    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'head': 'Update Crop Details',
        'page_nick': 'fd-update',
        'form': form,
        'crop_id': pk
    }
    return render(request, 'settings/update_crop.html', context)

@login_required# create crop
def add_crop(request):
    if request.method == 'POST':
        form = AddCropForm(request.POST)
        if form.is_valid():
            crop = form.save()
            messages.success(
                request, f'New Crop%s was successfully created.' % (crop.cropName))
            return redirect('show-crops')
    else:
        form = AddCropForm()
        
    gen_settings = Settings.objects.get(id=1)

    context = {
        'main_farm': gen_settings.main_farm,
        'title': 'Add Crop',
        'head': 'Add Crop',
        'form': form
    } 
    return render(request, 'settings/addcrops.html', context)

@login_required
def general_info(request):
	data = get_object_or_404(Settings, pk=1)
	form = GeneralInfoForm(request.POST or None, instance=data)

	if form.is_valid():
		form.save()
		messages.success(request, "Farm info was successfully updated.")
		request.session['main_farm'] = data.main_farm
		return redirect('general-info')

	context = {
		"page_nick": 'general-info',
        'title': 'Settings',
		"head" : "Settings",
		"form": form,
		"main_farm": data
	}
	return render(request, "settings/s_home.html", context)