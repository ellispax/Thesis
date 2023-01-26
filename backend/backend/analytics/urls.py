from django.urls import path
from .import views


urlpatterns = [

    path('', views.measurements_view, name='measurements-show'),
    #path('graph-show', views.graph_show, name='graph-show'),
    path('measurements-show', views.measurements_view, name='measurements-show'),
    # path('graph-present/<int:pk>/<dt>', views.graph_present, name='graph-present'),
    # path('chart', views.line_chart, name='line_chart'),
    # path('chartJSON', views.line_chart_json, name='line_chart_json'),
    
]