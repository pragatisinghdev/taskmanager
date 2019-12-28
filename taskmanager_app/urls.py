from django.urls import path, include
from . import views

app_name = 'taskmanager_app'
urlpatterns = [
		path('', views.index),
		path('dashboard/', views.dashboard, name='dashboard'),
		path('id=<int:pk>', views.project_details, name='project_detail')
	]