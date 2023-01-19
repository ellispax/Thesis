from django.shortcuts import render

# Create your views here.

def graph_show(request):
    context = {
        'title': 'Analytics',
        'head': 'Analytics',
        #'farms': farms
    }
    return render(request , 'analytics/index.html', context)