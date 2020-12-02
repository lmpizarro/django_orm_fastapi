#!/usr/bin/env python
'''
https://github.com/masnun/django-orm-standalone/blob/master/main.py
'''

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbManagement.settings')

WSGI = False

if WSGI:
    from django.core.wsgi import get_wsgi_application

    def init():
        application = get_wsgi_application()
else:
    from django.core.asgi import get_asgi_application

    def init():
        application = get_asgi_application()


    
init()
