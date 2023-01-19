
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Manage
# from employee.models import Employee, Employee_hiring_details
from transactions.models import Transaction
from settings.models import Settings

#from .forms import FarmAddForm

from django.contrib import messages
import xlwt
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def manage_show(request):
    man = Manage.objects.all()
    
    #print(man)

    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_farm'] = gen_settings.main_farm
    else:
        request.session['main_farm'] = ""
    # return render(request, 'hrms/dashboard.html', context)

    context = {
        'title': 'manage',
        'head': 'Manage',
        'farms': man
    }
    return render(request, 'manager/index.html', context)