from django.conf.urls import url
from .views import index_page

urlpatterns = [
    url(r'^$', index_page.as_view() , name='home'),
]
