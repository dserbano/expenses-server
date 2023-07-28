#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    python manage.py makemigrations
    python manage.py migrate
    python manage.py test expenses


    echo "PostgreSQL started"
fi


exec "$@"