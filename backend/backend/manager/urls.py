from django.urls import path

from . import views

urlpatterns = [
	path("", views.manage_show, name="manage"),
	path("manage-show", views.manage_show, name="manage-show"),
	

]