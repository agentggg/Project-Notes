import os
import sys
import django

# Ensure the correct path is included
# sys.path.insert(0, os.path.abspath("../"))  # Adjust if needed
sys.path.insert(0, os.path.abspath("../Backend"))  # Ensure backend is found

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Adjust if it's 'raw_app.settings'

# Initialize Django
django.setup()

print("Django setup successful!")