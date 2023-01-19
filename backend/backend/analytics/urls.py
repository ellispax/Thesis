from django.urls import path
from .import views


urlpatterns = [
    path('', views.graph_show, name='graph-show'),
    path('graph-show', views.graph_show, name='graph-show'),
    
]