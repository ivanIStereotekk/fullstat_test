FROM python:3.10.0

MAINTAINER Ivan Goncharov <ivan.stereotekk@gmail.com>

COPY ./requirements.txt  /app/requirements.txt


RUN pip install --upgrade pip

RUN pip install --no-cache-dir  -r /app/requirements.txt

COPY . /app

COPY ./entrypoint.sh  /app

WORKDIR /app/project_dir

VOLUME /project_dir/static/

ENTRYPOINT ["sh", "/entrypoint.sh"]

EXPOSE 8000

