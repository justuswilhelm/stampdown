release: ./manage.py migrate --noinput
web: gunicorn project.wsgi -w 3 -b "0.0.0.0:$PORT"
