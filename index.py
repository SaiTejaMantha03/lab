import os
import sys

# Add the Labs directory to the Python path
path = os.path.dirname(os.path.abspath(__file__))
labs_path = os.path.join(path, "Labs")

if labs_path not in sys.path:
    sys.path.append(labs_path)

# Initialize the Django WSGI application from Labs/lab/wsgi.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab.settings")

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
