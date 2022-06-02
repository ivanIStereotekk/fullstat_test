
from requests import request
from .serializers import Request_JSON_Serializer
import json

from celery import shared_task



@shared_task
def get_dataset_outer():
    _req = request.get('https://jservice.io/api/random?count=1')
    my_json = (json.dumps(_req.text))
    serializer = Request_JSON_Serializer(data=my_json)
    if serializer.is_valid():
        serializer.save()
    return "json_data loded successfully!"

@shared_task
def say_hello():
    hello = 'Hello Vasya!'
    return print(hello)


from celery.schedules import crontab
from ..project_dir.celery import c_app
c_app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.get_dataset_outer',
        'schedule': crontab(hour=0, minute=1, day_of_week=1),
        'args': (16, 16),
    },
}