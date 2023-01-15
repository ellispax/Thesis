
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Farm 
# from employee.models import Employee, Employee_hiring_details
# from logs.models import Logs
from settings.models import Settings

from .forms import FarmAddForm

from django.contrib import messages
import xlwt
from datetime import datetime, timedelta
from django.db.models import Q
from django.contrib.auth.decorators import login_required



@login_required
def dashboard(request):
    
    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'title': 'farm',
        'head': 'Farms'
    }
    
    if gen_settings:
        request.session['main_farm'] = gen_settings.main_farm
    else:
        request.session['main_farm'] = ""
    return render(request, 'home/dashboard.html', context)



@login_required
def farm_show(request):
    farms = Farm.objects.all()
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_farm'] = gen_settings.main_farm
    else:
        request.session['main_farm'] = ""
    # return render(request, 'hrms/dashboard.html', context)

    context = {
        'title': 'farm',
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
            action = f"created farm '{farm.farm_name}'"
            Logs.objects.create(action=action, action_by=request.user, action_date=datetime.now())

            messages.success(
                request, f'New Farm%s was successfully created.' % (farm.farm_name))
            return redirect('farm-show')
    else:
        form = FarmAddForm()
        
    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'head': 'Add Farm',
        'form': form
    }
    return render(request, 'home/farm_add.html', context)