release: python manage.py migrate --noinput
web: gunicorn workflowengine.wsgi
worker: celery -A workflowengine worker
