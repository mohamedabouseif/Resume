from django.conf.urls import url
from .views import resume_page 

urlpatterns = [
    url(r'^', resume_page.as_view(), name='resume'),
   
]
