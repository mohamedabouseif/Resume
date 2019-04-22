from django.views.generic import ListView , DetailView
from django.shortcuts import render,get_object_or_404
from .models import info_data
# Create your views here.

class index_page(ListView):
	template_name ='home/home.html'
	queryset =info_data.objects.all()