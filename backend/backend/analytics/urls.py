from django.urls import path
from .import views


urlpatterns = [

    path('', views.measurements_view, name='measurements-show'),
    
    path('measurements-show', views.measurements_view, name='measurements-show'),
    
    
]