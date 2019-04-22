from django.contrib import admin
from .views import project
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	list_display=['__str__','slug']
	class meta :
		model = project

admin.site.register(project)