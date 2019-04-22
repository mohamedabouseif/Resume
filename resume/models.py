import random
import os
from django.db import models

# Create your models here.


def get_filename_ext(filePath):
	base_name  = os.path.basename(filePath)
	name , ext = os.path.splitext(base_name)
	return name ,ext



def upload_file_path(instance , filename):
	new_fileName = random.randint(1,39545215846555)
	name ,ext = get_filename_ext(filename)
	final_filename = '{new_fileName}{ext}'.format(new_fileName=new_fileName,ext=ext)
	return "{new_fileName}/{final_filename}".format(
		new_fileName=new_fileName,
		final_filename=final_filename)


class tech_train(models.Model):
	title  =models.CharField(max_length=500)
	tech_train_url  =models.CharField(max_length=500)

	def __str__(self):
		return self.title

class skill(models.Model):
	skills      =models.CharField(max_length=100)

	def __str__(self):
		return self.skills

class interest(models.Model):
	interests   =models.CharField(max_length=500 )

	def __str__(self):
		return self.interests

class MyResume(models.Model):
	title =models.CharField(max_length=50)
	file  =models.FileField(upload_to='upload_file_path' ,null =False)

	def __str__(self):
		return self.title

	



