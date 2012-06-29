import os
import sys
import site

site.addsitedir('/home/eventhub/.virtualenvs/eventhub/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'eventhub.settings'

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

