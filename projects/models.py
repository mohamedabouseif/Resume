import random
import os
from django.db import models
from django.db.models.signals import pre_save ,post_save
from django.urls import reverse
from .utils import unique_slug_generator

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



class project(models.Model):

	title       =models.CharField(max_length=50)
	slug        = models.SlugField(blank=True, unique = True)
	link        =models.CharField(max_length=100)
	image       =models.FileField(upload_to=upload_image_path, null= True )
	description =models.CharField(max_length=200)


	def get_absolute_url(self):
		# return "/projects_page/{slug}".format(slug=self.slug)
		return reverse("projects_page:detail",kwargs={"slug":self.slug})


	def __str__(self):
		return self.title


	




def project_pre_save_reciever(sender,instance , *args ,**kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(project_pre_save_reciever , sender=project)