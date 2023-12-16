#!/bin/sh

echo "export SECRET_KEY='$(openssl rand -hex 40)'" > ./.DJANGO_SECRET_KEY
. ./.DJANGO_SECRET_KEY

python manage.py runserver 0.0.0.0:8000
