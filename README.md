# fullstat_test

Description of testtask (file): 
- goals and tasks.txt


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

Creating superuser:
---------------------
- $  docker exec -it container_id bash
- $  python manage.py createsuperuser
- ...follow steps 
 
Making migrations:
---------------------
- $  docker exec -it container_id bash
- $  python manage.py migrate



- IMPORTANT - Into admin panel[periodic tasks] you should put Positional Arguments :



RESTful backend service [demo]:
----------------------


API documentation: http://localhost/swagger

For test operations go to - http://localhost/redoc






