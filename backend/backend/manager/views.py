
from django.shortcuts import render, redirect, get_object_or_404
from .models import Manage
from transactions.models import Transaction
from settings.models import Settings
from .forms import ManageUpdateForm
from django.contrib import messages
import xlwt
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
        'title': 'Manage Settings Display',
        'head': 'Manage',
        'farms': man
    }
    return render(request, 'manager/index.html', context)


@login_required
def manage_updateview(request, pk):
    manage = get_object_or_404(Manage, id=pk)
    # try:
    #     sts = Farm.objects.get(pk = pk)

    #     if sts:
    #         STATUS = sts.status
    # except:

    #     print("The user doesn't exist")

    if request.method == 'POST':
        # form = FarmAddForm(request.POST or None, instance=farm)
        form = ManageUpdateForm(request.POST or None, instance=manage)
        # if STATUS == 1:
        #     action = 0
        # else:
        #     action = 1
        if form.is_valid():
            form.save()
            #action = ""
            # Transaction.objects.create(action=action, action_by=request.user, farm_id = pk, action_date=datetime.now(),action_time=timezone.now())
            messages.success(request, f'Pre-set Values were successfully updated.')
            return redirect('manage-show')
    else:
        # form = FarmAddForm(instance=farm)
        form = ManageUpdateForm(instance=manage)


    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'title': 'Update Manage Settings',
        'head': 'Update Manage Settings',
        'page_nick': 'fd-update',
        'form': form,
        'farm_id': pk
    }
    return render(request, 'manager/update.html', context)