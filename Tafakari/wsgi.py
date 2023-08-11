import os

from django.core.wsgi import get_wsgi_application
"""
get_wsgi_application is a function provided by the Django web framework in Python.
It is used to create a WSGI (Web Server Gateway Interface) application object, which acts as
an interface between a web server and a Python web application.

"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tafakari.settings')

application = get_wsgi_application()
app = application
