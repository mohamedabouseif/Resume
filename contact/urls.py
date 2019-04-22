from django.conf.urls import url
from .views import ContactCreate ,success 
urlpatterns = [
    url(r'^$',ContactCreate.as_view() , name='contact'),
    url(r'^MessgaeSent/$',success.as_view() , name='msg_sent'),
 
]
