FROM python:3.10.0

MAINTAINER Ivan Goncharov <ivan.stereotekk@gmail.com>

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip



RUN pip install --no-cache-dir  -r /app/requirements.txt


COPY . /app


EXPOSE 8000


ENTRYPOINT ["/app/project_dir/create_superuser_script.sh","/app/project_dir/project_dir/celery_commands.sh"]


CMD ["python", "manage.py", "runserver", "0.0.0.0", "--port", "8000"]

