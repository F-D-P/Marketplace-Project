web: gunicorn ecoen_project.wsgi:application
release: python manage.py migrate && python manage.py collectstatic --noinput
