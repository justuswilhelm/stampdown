release: ./manage.py migrate --noinput
web: gunicorn stampdown.wsgi -w 3 -b "0.0.0.0:$PORT"
