import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_app_django_react.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_ADMIN_USERNAME")
email = os.environ.get("DJANGO_ADMIN_EMAIL")
password = os.environ.get("DJANGO_ADMIN_PASSWORD")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superuser created.")
else:
    print("ℹ️ Superuser already exists.")
