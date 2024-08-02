#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
# pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Build Tailwind CSS
npx tailwindcss -i ./static/css/dist/styles.css -o ./static/css/dist/output.css --minify
