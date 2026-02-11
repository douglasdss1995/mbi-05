"""
ASGI config for sale project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< Updated upstream
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
>>>>>>> Stashed changes
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sale.settings')

application = get_asgi_application()
