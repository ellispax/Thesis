from django.shortcuts import render
from .models import measurements
from django.views.generic import TemplateView
#from chartjs.views.lines import BaseLineChartView

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .models import measurements
#from .serializers import MeasurementSerializer
import json
import datetime
from django.db.models import Q


from django.shortcuts import render
from .models import measurements

title = "Analytics Display"

def measurements_view(request):
    farms = measurements.objects.all()
    if request.method == 'POST':
        farm_id = request.POST.get('farm_id')
        date = request.POST.get('date')
        Measurements = measurements.objects.filter(farm=farm_id, date=date)
        return render(request, 'analytics/blank.html', {'measurements': Measurements, 'farms': farms, 'title': title, 'date': date})
    else:
        return render(request, 'analytics/blank.html', {'farms': farms, 'title': title})





# def graph_show(request):
    
#     date = '<Date Here>'
#     context = {
#         'title': 'Analytics',
#         'head': 'Analytics',
#         'date': date
#         #'farms': farms
#     }
#     return render(request , 'analytics/blank.html', context)

# def graph_present(request, pk, dt):
#     x = measurements.objects.filter(farm_id = pk)
#     vls = x.objects.filter(date = dt)
#     vt,vp,vh,vm, tm = [],[],[],[], []

#     for i in vls:
        
#         tm.append(i.time)
#         vt.append(i.temp)
#         vp.append(i.pH)
#         vh.append(i.humidity)
#         vm.append(i.moisture)
    

#     def get_labels(self):
        
#         """Return 7 labels for the x-axis."""
#         #return ["January", "February", "March", "April", "May", "June", "July"]
#         return tm

#     def get_providers(self):
#         """Return names of datasets."""
#         #return ["Central", "Eastside", "Westside"]
#         return["Temp(*c)", "pH", "Humidity (%)", "Moisture (kg)"]
        

#     def get_data(self):  
       
       
#         """Return 3 datasets to plot."""
#         print(vt)
#         # return [[75, 44, 92, 11, 44, 95, 35],
#         #         [41, 92, 18, 3, 73, 87, 92],
#         #         [87, 21, 94, 3, 90, 13, 65]]
#         return [vt,vp,vh,vm]

#     line_chart = TemplateView.as_view(template_name='line_chart.html')
    
#     line_chart_json = LineChartJSONView.as_view()


#     context = {
#         'title':'analytics',
#         'head': 'Analytics',
#         'date': dt
#     }

#     return render(request, 'analytics/blank.html', context)

# class LineChartJSONView(BaseLineChartView):
#     global vals, vt,vp,vh,vm, tm
#     vals = measurements.objects.filter(farm_id = 1)
#     #vals.filter(date = dt)
#     vt,vp,vh,vm, tm = [],[],[],[], []
#     for i in vals:
        
#         tm.append(i.time)
#         vt.append(i.temp)
#         vp.append(i.pH)
#         vh.append(i.humidity)
#         vm.append(i.moisture)
#     #print(type(vals))

#     def get_labels(self):
        
#         """Return 7 labels for the x-axis."""
#         #return ["January", "February", "March", "April", "May", "June", "July"]
#         return tm

#     def get_providers(self):
#         """Return names of datasets."""
#         #return ["Central", "Eastside", "Westside"]
#         return["Temp(*c)", "pH", "Humidity (%)", "Moisture (kg)"]
        

#     def get_data(self):
        
       
       
#         """Return 3 datasets to plot."""
#         print(vt)
#         # return [[75, 44, 92, 11, 44, 95, 35],
#         #         [41, 92, 18, 3, 73, 87, 92],
#         #         [87, 21, 94, 3, 90, 13, 65]]
#         return [vt,vp,vh,vm]


# line_chart = TemplateView.as_view(template_name='line_chart.html')
# line_chart_json = LineChartJSONView.as_view()