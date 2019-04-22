from django.conf.urls import url
from .views import projects_list ,projectDetail

urlpatterns = [
    url(r'^$',projects_list.as_view() , name='projects'),
    url(r'^(?P<slug>[\w-]+)/$',projectDetail.as_view(),name ='detail'),

]
