#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies (para Tailwind CSS)
npm install

# Convert static asset files
python manage.py collectstatic --no-input

# Build Tailwind CSS
npx tailwindcss -i ./static/css/styles.css -o ./static/css/output.css --minify

# Apply any outstanding database migrations
python manage.py migrate
