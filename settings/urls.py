from django.urls import path

from . import views

urlpatterns = [
	path("", views.general_info, name="settings"),
	path("general-info", views.general_info, name="general-info"),
	path('update-show', views.update_show, name='update-show'),
    path('show-crops', views.show_crops, name='show-crops'),
	path('users', views.get_users, name='users'),
    path('add-crop', views.add_crop, name='add-crop'),
	path('add-user', views.add_user, name='add-user'),
	path("update-view/<int:pk>", views.update_farm, name="update-view"),
    path("update-crop/<int:pk>", views.update_crop, name="update-crop"),
	path("delete-crop/<int:pk>", views.delete_crop, name="delete-crop"),
	path("delete-farm/<int:pk>", views.delete_farm, name="delete-farm"),

	

]