import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knot_and_crafts.settings')
application = get_wsgi_application()
