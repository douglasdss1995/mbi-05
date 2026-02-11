"""
WSGI config for sale project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< Updated upstream
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
>>>>>>> Stashed changes
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sale.settings')

application = get_wsgi_application()
