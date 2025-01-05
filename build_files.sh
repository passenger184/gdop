#!/bin/bash

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Create Vercel-compatible output vercel directory
mkdir -p .vercel/output/static
cp -r staticfiles/ .vercel/output/static/

python3 manage.py makemigrations
python3 manage.py migrate

# Seed the database
python manage.py seed

# Create a default superuser
python3 manage.py shell <<EOF
from django.contrib.auth.models import User
username = "admin"
password = "admin123"
email = "admin@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully.")
else:
    print(f"Superuser '{username}' already exists.")
EOF
