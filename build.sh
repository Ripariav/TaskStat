#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies (uncomment if needed)
# pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Build Tailwind CSS
npx tailwindcss -i ./staticfiles/css/styles.css -o ./staticfiles/css/output.css --minify
