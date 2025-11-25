release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn Prog_EcoEn.ecoen_project.wsgi:application
