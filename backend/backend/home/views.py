
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Farm 
# from employee.models import Employee, Employee_hiring_details
from transactions.models import Transaction
from settings.models import Settings

from .forms import FarmAddForm, FarmToggleStatus

from django.contrib import messages
import xlwt
from datetime import datetime, timedelta
from django.utils import timezone
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


# def company_gov_deducts(request, pk):
#     company = get_object_or_404(Company_rates, company=pk)
    
#     if request.method == 'POST':
#         form = CompanyGovDeduct(request.POST or None, instance=company)
#         if form.is_valid():
#             form.save()

#             action = f"{company} deductions has been updated. sss={request.POST['sss']}, philhealth={request.POST['philhealth']}, pagibig={request.POST['pagibig']}"
#             Logs.objects.create(action=action, action_by=request.user, action_date=datetime.now())

#             messages.success(request, f'Company Government deductions was successfully updated.')
#             return redirect('company-gov-deducts', pk=pk)
#     else:
#         form = CompanyGovDeduct(instance=company)

#     gen_settings = General_settings.objects.get(id=1)
#     context = {
#         'main_company': gen_settings.main_company,
#         'page_nick': 'gov-deducts',
#         'head': 'Update Government Deductions',
#         'form': form,
#         'company_id': pk
#     }
#     return render(request, 'hrms/company_update.html', context)