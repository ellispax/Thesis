from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Settings
from .forms import GeneralInfoForm
from django.contrib import messages
from home.models import Farm
from home.forms import FarmAddForm

def update_show(request):
    farms = Farm.objects.all()
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_farm'] = gen_settings.main_farm
    else:
        request.session['main_farm'] = ""
    # return render(request, 'hrms/dashboard.html', context)

    context = {
        'title': 'farm',
        'head': 'Farms Details Update',
        'farms': farms
    }
    return render(request, 'settings/all_farms.html', context)


def update_view(request, pk):
    farm = get_object_or_404(Farm, id=pk)
    # try:
    #     sts = Farm.objects.get(pk = pk)

    #     if sts:
    #         STATUS = sts.status
    # except:

    #     print("The user doesn't exist")

    if request.method == 'POST':
        form = FarmAddForm(request.POST or None, instance=farm)
        # if STATUS == 1:
        #     action = 0
        # else:
        #     action = 1
        if form.is_valid():
            form.save()
            #action = ""
            # Transaction.objects.create(action=action, action_by=request.user, farm_id = pk, action_date=datetime.now(),action_time=timezone.now())
            messages.success(request, f'Farm Details were successfully updated.')
            return redirect('update-show')
    else:
        form = FarmAddForm(instance=farm)


    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_farm': gen_settings.main_farm,
        'head': 'Update Farm Details',
        'page_nick': 'fd-update',
        'form': form,
        'farm_id': pk
    }
    return render(request, 'settings/update_farm.html', context)



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
		"head" : "Settings",
		"form": form,
		"main_farm": data
	}
	return render(request, "settings/s_home.html", context)