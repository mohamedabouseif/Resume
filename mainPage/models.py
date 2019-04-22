import random
import os
from django.db import models
from django.urls import reverse


# Create your models here.

def get_filename_ext(filePath):
	base_name  = os.path.basename(filePath)
	name , ext = os.path.splitext(base_name)
	return name ,ext



def upload_image_path(instance , filename):
	new_fileName = random.randint(1,39545215846555)
	name ,ext = get_filename_ext(filename)
	final_filename = '{new_fileName}{ext}'.format(new_fileName=new_fileName,ext=ext)
	return "product/{new_fileName}/{final_filename}".format(
		new_fileName=new_fileName,
		final_filename=final_filename)



class info_data(models.Model):
	name      =models.CharField(max_length=45)
	career    =models.CharField(max_length=30)
	address   =models.CharField(max_length=50)
	education =models.CharField(max_length= 70)
	email     =models.EmailField(max_length=254)
	mobile    = models.CharField(max_length=23)
	photo     =models.FileField(upload_to=upload_image_path, null= True )

	def __str__(self):
		return self.name


