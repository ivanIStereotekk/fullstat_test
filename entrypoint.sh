#!/bin/sh

python manage.py migrate --no-input

python manage.py collectstatic --no-input

gunicorn project_dir.wsgi:application --bind 0.0.0.0:8000

celery -A project_dir worker -l INFO

celery -A project_dir beat -l INFO





