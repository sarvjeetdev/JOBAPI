import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JobAPI.settings')

# This is your WSGI application
application = get_wsgi_application()

# Wrap it with WhiteNoise to serve static files
application = WhiteNoise(application)
