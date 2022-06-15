FROM python:3.10.0-alpine

MAINTAINER Ivan Goncharov <ivan.stereotekk@gmail.com>

WORKDIR /app/project_dir

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT ["/app/create_superuser_script.sh"]


CMD ["python", "manage.py", "runserver", "0.0.0.0", "--port", "8000"]