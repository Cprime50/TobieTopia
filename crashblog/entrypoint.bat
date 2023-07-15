@echo off

echo Running "python manage.py migrate"  
python manage.py migrate    

echo Running "python manage.py collectstatic"
python manage.py collectstatic

echo Running "gunicorn crashblog.wsgi:application --bind 0.0.0.0:8000"
gunicorn crashblog.wsgi:application --bind 0.0.0.0:8000


