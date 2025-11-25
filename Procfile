release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn ecoen_project.wsgi:application
