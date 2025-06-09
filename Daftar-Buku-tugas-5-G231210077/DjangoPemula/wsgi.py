
"""
WSGI config for DjangoPemula project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoPemula.settings')

application = get_wsgi_application()
