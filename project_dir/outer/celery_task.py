from celery import Celery
from time import sleep
from requests import request
from .serializers import Request_JSON_Serializer
import json


app = Celery()

@app.add_periodic_task()
def get_dataset_outer():
    _req = request.get('https://jservice.io/api/random?count=1')
    my_json = (json.dumps(_req.text))
    serializer = Request_JSON_Serializer(data=my_json)
    if serializer.is_valid():
        serializer.save()
    return "json_data loded successfully!"


