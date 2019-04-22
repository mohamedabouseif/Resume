from django.views.generic import ListView 
from django.shortcuts import render ,get_object_or_404
from .models import tech_train ,skill ,interest ,MyResume
# Create your views here.

class resume_page(ListView):
	template_name="resume/resume.html"
	queryset=tech_train.objects.all()

	def get_context_data(self,*args,**kwargs):
		context =super(resume_page,self).get_context_data(*args,**kwargs)
		context['skills']=skill.objects.all()
		context['interest']=interest.objects.all()
		context['cv']=MyResume.objects.all()
		
		return context


