import os
from django.conf import settings
from django.db import models

# Create your models here.
def images_path():
    return os.path.join(settings.BASE_DIR, '../taskmanager_app/static')


class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	file = models.FilePathField(path=images_path)
	#author = models.ForeignKey('User', on_delete='models.CASCADE', blank=True, default=False)
	end_date = models.DateField()


class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length= 50, blank=True)
	phone = models.CharField(max_length=100, blank=True)
