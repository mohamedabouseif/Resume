from .base import *

DEBUG = False

ALLOWED_HOSTS = ['mohamedabouseif.binkfe.com']


DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'faried',
        'HOST':'mysql.jesrat.internal',
        'PASSWORD':'f4r!3dP4$$w',
        'USER':'farieduser',
        'PORT':'3306',

    }
}



