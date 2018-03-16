import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wangda.settings")

from django.core.wsgi import get_wsgi_application
from wangda import restaurant as application 

if __name__ == "__main__":
    application.run()

try:
    application = get_wsgi_application()
    print 'WSGI without exception'
except Exception as err:
    print err
