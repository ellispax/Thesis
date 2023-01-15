from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Settings
from .forms import GeneralInfoForm
from django.contrib import messages


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