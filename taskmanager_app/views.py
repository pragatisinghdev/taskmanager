from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Project
# Create your views here.

def index(request):
	return HttpResponse("This is index")

def dashboard(request):
	all_projects = Project.objects.all()
	return render(request, 'taskmanager_app/dashboard.html', {'projects':all_projects})

def project_details(request, pk):
	project = Project.objects.get(pk=pk)
	if not project:
		return HttpResponseNotFound(f"The Project for Id {pk} does not exist.")

	return render(request, 'taskmanager_app/project_details.html', {'project':project})
