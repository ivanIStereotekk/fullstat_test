# fullstat_test
Backend (приложение) app Django/Celery/Redis/PostgresSQL
------
Модель бекенд приложения:
-----

Описаны ОРМ модели User, Publication, Reaction, Link.

JWT аутентификация

Эндпоинты для работы со всеми обьектами/моделями GET,POST,PUT,UPDATE,DELETE.

Фильтры для поиска уникальных наборов данных.

Планировщик задач с возможностью настройки времени/частоты выполнения (запросы к внешним ресурсам, рассылки пуш уведомлений).

Docker-Compose

По своей сути модель приложения близка к социальной сети в купе с сайтом/доской объявлений.

Описание:

USER/Пользователь сайта:
------
Регистрация, авторизация, аутентификация,(JWT и Token-Uathentication),сброс пароля, подтверждение сброса в письме.

Пользователь может публиковать и править записи(статьи или объявления).

Получать записи других пользователей.

Получать записи по датам.

Получать записи по рейтингу.

Получать реакции пользователей (likes).

Получать записи по slug.

Получать уникальные наборы записей. 


---------
Есть настроенная админ панель:

На ней можно настраивать Celery

Править и анализировать записи

-----------------------
Сконфигурирован NGINX прокси

Для быстрого запуска и проверки рекомендую воспользоваться Docker-Compose.

Запустите Docker

Образы тут: https://hub.docker.com/r/stereotekk/fullstat/tags

Дерните репозиторий.

В рабочей директории $docker-compose build...ждите пока соберется образ.








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



IMPORTANT - Into admin panel[periodic tasks] you should put Positional Arguments :
---



RESTful backend service:
----------------------


API documentation: http://localhost/swagger

For test operations go to - http://localhost/redoc

API url's:
-----

<img width="448" alt="API list" src="https://user-images.githubusercontent.com/18102432/175573627-1c37deae-fafd-4dac-9ed0-f0352141834c.png">

Auth/Token URL's:
----

<img width="456" alt="Auth Api" src="https://user-images.githubusercontent.com/18102432/175573816-30602e73-128e-4715-8363-d32728a4a7e2.png">








