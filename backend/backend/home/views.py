
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Farm 
from datetime import date

from transactions.models import Transaction
from settings.models import Settings

from .forms import FarmAddForm, FarmToggleStatus

from django.contrib import messages
import xlwt
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from manager.models import Manage
from crops.models import   Crops
import requests, json




@login_required
def dashboard(request):
   # q={city name}
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=london&units=metric&appid=c263e33729247d585b1bf41636fc4062")
    

    #response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=6.2088&lon=106.8456&units=metric&appid=c263e33729247d585b1bf41636fc4062")
    
    #response = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=-19.45132100&lon=29.81773900&exclude=hourly,daily&appid=c263e33729247d585b1bf41636fc4062")
    
    if response.status_code == 200:
        weather_data = response.json()
        w_data = weather_data['main']
        temp = w_data['temp']
        temp_max = w_data['temp_max']
        temp_min = w_data['temp_min']
        humidity = w_data['humidity']
        pressure = w_data['pressure']
        rain_data = weather_data['weather']
        rain_desc = rain_data[0]['description']
        print(temp, temp_min, temp_max, humidity, pressure, rain_desc)
    else:
        print("Error in the HTTP request")
        temp = 'err'
        humidity = 'err'
        pressure = 'err'
        rain_desc = 'err'
        temp_max = 'err'
        temp_min = 'err'

    
    dt = date.today()
    
    farms = Farm.objects.all()

    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'title': 'farm',
        'head': 'Farms',
        'farms': farms,
        'date' : dt,
        'temp' : temp,
        'tempMin': temp_min,
        'tempMax': temp_max,
        'humidity': humidity,
        'rain': rain_desc,
        'pressure': pressure,
    }
    
    if gen_settings:
        request.session['main_farm'] = gen_settings.main_farm
    else:
        request.session['main_farm'] = ""
    return render(request, 'home/dashboard.html', context)



@login_required
def farm_show(request):
    farms = Farm.objects.all()

    print(farms)
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_farm'] = gen_settings.main_farm
    else:
        request.session['main_farm'] = ""
    # return render(request, 'hrms/dashboard.html', context)

    context = {
        'title': 'Farm Display',
        'head': 'Farms',
        'farms': farms
    }
    return render(request, 'home/all_farms.html', context)


@login_required# create farm
def farm_add(request):
    # user = get_object_or_404(User, user=request.user)
    if request.method == 'POST':
        form = FarmAddForm(request.POST)
        if form.is_valid():
            farm = form.save()

            selected_crop = form.cleaned_data['crop']

            # get the crop object from the database
            crop = Crops.objects.get(cropName=selected_crop)

            # create a new Manage object with the newly created farm as the foreign key
            manage = Manage.objects.create(farm=farm, temp=crop.temp, humidity=crop.humidity, moisture=crop.moisture, pH=crop.pH, water=crop.water_needed)
            #create a new row in the manage tab with same id as the new farm and vaues set to 0
            action = f"created farm '{farm.farm_name}'"

            #Logs.objects.create(action=action, action_by=request.user, action_date=datetime.now())

            messages.success(
                request, f'New Farm%s was successfully created.' % (farm.farm_name))
            return redirect('farm-show')
    else:
        form = FarmAddForm()
        
    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'title': 'Add Farm',
        'head': 'Add Farm',
        'form': form
    } 
    return render(request, 'home/farm_add.html', context)


@login_required
def farm_update(request, pk):
    farm = get_object_or_404(Farm, id=pk)
    try:
        sts = Farm.objects.get(pk = pk)

        if sts:
            STATUS = sts.status
    except:

        print("The user doesn't exist")

    if request.method == 'POST':
        # form = FarmAddForm(request.POST or None, instance=farm)
        form = FarmToggleStatus(request.POST or None, instance=farm)
        if STATUS == 1:
            action = 0
        else:
            action = 1
        if form.is_valid():
            form.save()
            #action = ""
            Transaction.objects.create(action=action, action_by=request.user, farm_id = pk, action_date=datetime.now(),action_time=timezone.now())
            messages.success(request, f'Farm Status was successfully updated.')
            return redirect('farm-show')
    else:
        form = FarmToggleStatus(instance=farm)


    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'head': 'Update Farm Status',
        'page_nick': 'f-update',
        'form': form,
        'farm_id': pk
    }
    return render(request, 'home/farm_update.html', context)

def weather(request):
    

    context = {
        
    }
    return render(request, 'home/notice-cards.html', context)
    

