release: python manage.py makemigrations && python manage.py migrate

web: gunicorn wanderlust_api.wsgi
