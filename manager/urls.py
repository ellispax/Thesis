from django.urls import path

from . import views

urlpatterns = [
	path("", views.manage_show, name="manage"),
	path("manage-show", views.manage_show, name="manage-show"),
	path("manage-update-view/<int:pk>", views.manage_updateview, name="manage-update-view"),
	

]