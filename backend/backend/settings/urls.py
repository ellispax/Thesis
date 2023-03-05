from django.urls import path

from . import views

urlpatterns = [
	path("", views.general_info, name="settings"),
	path("general-info", views.general_info, name="general-info"),
	path('update-show', views.update_show, name='update-show'),
    path('show-crops', views.show_crops, name='show-crops'),
    path('add-crop', views.add_crop, name='add-crop'),
	path("update-view/<int:pk>", views.update_farm, name="update-view"),
    path("update-crop/<int:pk>", views.update_crop, name="update-crop"),
	# path("<int:id>/eeconrib_update/", views.sss_rates_update, name="eecontrib-update"),
	# path("<int:id>/eeconrib_delete/", views.sss_rates_delete, name="eecontrib-delete"),
	# path("eeconrib_create/", views.sss_rates_create, name="eecontrib-create"),
	# path("bank_options", views.bank_options, name="bank-options"),

]