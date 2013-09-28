import os
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "outpatient.settings.production")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "outpatient.settings.production")
import dj_static
# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
