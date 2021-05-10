#!/bin/bash

# Install dependencies
# pip install -r requirements.txt

# Execute startup scripts
#echo "Applying Collet static"
#python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate


service supervisor start
python manage.py runserver 0.0.0.0:80
