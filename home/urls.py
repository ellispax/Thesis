from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('farm-show', views.farm_show, name='farm-show'),    
    path('farm-update/<int:pk>', views.farm_update, name='farm-update'),   
    path('farm-add', views.farm_add, name='farm-add'),
]