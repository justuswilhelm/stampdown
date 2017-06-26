# project

## Requirements
- bower
- npm
- python3.5
- PostgreSQL

## NPM

This will take care of downloading bower assets as well
```
npm install
```

## Heroku Config

- heroku/nodejs
- heroku/python

```
echo "heroku/nodejs" "heroku/python" | xargs -n 1 heroku buildpacks:add
```

Set `SECRET_KEY` to something random

```
heroku create "project"
heroku config:set SECRET_KEY=(openssl rand 12 -base64)
heroku config:set ALLOWED_HOSTS=project.herokuapp.com
heroku run --no-tty ./manage.py migrate
heroku run --no-tty ./manage.py createsuperuser
printf "Site.objects.create(name="project", domain="project.herokuapp.com")\n" | heroku run --no-tty ./manage.py shell_plus --ipython
```
