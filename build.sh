#!/usr/bin/env bash
# Exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Convertir archivos estáticos
python manage.py collectstatic --no-input

# Aplicar cualquier migración pendiente
python manage.py migrate

# Construir Tailwind CSS
npx tailwindcss -i TaskStat/staticfiles/css/dist/styles.css -o TaskStat/staticfiles/css/dist/output.css --minify

# Explicitly install gunicorn (just in case)
pip install gunicorn