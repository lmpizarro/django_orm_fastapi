#!/usr/bin/env python
'''
https://github.com/masnun/django-orm-standalone/blob/master/main.py
'''

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbManagement.settings')
application = get_wsgi_application()


def test():
    #Add user
    user = Logger(message="masnun test")
    user.save()



