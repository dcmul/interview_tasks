#!/bin/bash

# Install dependencies
# pip install -r requirements.txt

# Execute startup scripts
# `python manage.py collectstatic --noinput



python manage.py migrate
service supervisor start
python manage.py runserver 0.0.0.0:80
