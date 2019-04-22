from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('mainPage.urls',namespace='main_page')),
    url(r'^resume/', include('resume.urls',namespace='resume_page')),
    url(r'^portofollio/', include('projects.urls',namespace='projects_page')),
    url(r'^contact/', include('contact.urls',namespace='contact_page')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
	urlpatterns =urlpatterns  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns =urlpatterns  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
