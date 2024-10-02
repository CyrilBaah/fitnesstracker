# !/bin/sh

python manage.py makemigrations

python manage.py migrate

gunicorn base.wsgi:application --workers 3 --bind [::]:8000 

