FROM python:3.10.0

MAINTAINER Ivan Goncharov <ivan.stereotekk@gmail.com>

COPY ./requirements.txt  /app/requirements.txt

COPY ./additional_reqs.txt  /app/additional_reqs.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir  -r /app/requirements.txt

RUN pip install --no-cache-dir  -r /app/additional_reqs.txt


COPY . /app


WORKDIR /app/project_dir

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
