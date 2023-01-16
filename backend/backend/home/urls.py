from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('farm-show', views.farm_show, name='farm-show'),
    # path('search-company', views.search_company, name='search-company'),
    path('farm-update/<int:pk>', views.farm_update, name='farm-update'),
    # path('print-employees/<int:pk>', views.print_employees, name='print-employees'),
    # path('company-rates/<int:pk>', views.company_rates, name='company-rates'),
    # path('company-gov-deducts/<int:pk>',
    #      views.company_gov_deducts, name='company-gov-deducts'),
    # path('company-other-options/<int:pk>',
    #      views.company_other_options, name='company-other-options'),
    path('farm-add', views.farm_add, name='farm-add'),
    # path('company-delete/<int:pk>', views.company_delete, name='company-delete')
]