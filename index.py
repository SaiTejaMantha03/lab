import os
import sys

# Define the root path (where index.py and vercel.json are)
root_path = os.path.dirname(os.path.abspath(__file__))
# Define the Labs path where manage.py and the apps are
labs_path = os.path.join(root_path, "Labs")

# Insert labs_path at the beginning of sys.path
if labs_path not in sys.path:
    sys.path.insert(0, labs_path)

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab.settings")

# Get the WSGI application
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
