# fullstat_test

Description of testtask (file): goals and tasks.txt


Stack:
---------------------
- Nginx 
- Gunicorn 
- Django
- Djangorestframework
- Celery
- Postgres
- Redis
- Swagger

![WSGI](https://user-images.githubusercontent.com/18102432/175305423-d381ef53-5ec6-462f-9c36-6808954cc444.jpeg)

Images on dockerhub - https://hub.docker.com/repository/docker/stereotekk/fullstat
----------------------



Steps to run:
----------------------
get repository on your local machine...

- $ docker-compose build
- $ docker-compose up

Don't forget $python manage.py createsuperuser - for using django admin



RESTful backend service [demo]:
----------------------

[ Base URL:localhost:80 ]

http://localhost/swagger/?format=openapi

For test operations go to - http://localhost/redoc/






