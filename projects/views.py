from django.views.generic import ListView , DetailView
from django.shortcuts import render,get_object_or_404
from .models import project
# Create your views here.
class projects_list(ListView):
	template_name = "project/projects.html"
	queryset =project.objects.all()



class projectDetail(DetailView):
	
	template_name ="project/project_detail.html"
	#queryset =project.objects.all()

	def get_object(self, *args,**kwargs):
		request = self.request
		slug    = self.kwargs.get('slug')
		try:
			instance = project.objects.get(slug=slug)
		except project.DoesNotExist:
			raise Http404("Not Found Mohamed ..")
		except project.MultipleObjectsReturned:
			qs = project.objects.filter(slug=slug , active = True)
			instance = qs.first()
		except:
			raise Http404("Offffff")
		return instance
