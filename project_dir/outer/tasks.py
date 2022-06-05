
from project_dir.celery import app
from outer.mailer import send
from celery import shared_task
import requests as req
from .models import Request_JSONB_Model

@shared_task
def add(x, y):
    return x + y
@shared_task
def mul(x, y):
    return x * y
@shared_task
def xsum(numbers):
    return sum(numbers)
#------------------------------

# My Tasks

#------PAYLOAD------
"""
Makes request to outer service and get paylad json then saves to database. Just for Example!
"""
@shared_task
def get_payload(items):
    try:
        _request = req.get(f'https://jservice.io/api/random?count={items}')
        new_obj = Request_JSONB_Model(payload=_request.text)
        new_obj.save()
    except Exception:
        return 'Something went wrong with outer service !'
    return 'Outer service data recieved !'
#--------SEND---LETTER's--------

@app.task
def send_letter():
    #----------
    mail_to = 'ivan.stereotekk@gmail.com'
    text = 'Много спама я вам пришлю!'
    subject = 'Hello my dear friend:'
    sender = 'capitan.django@mail.ru'
    #----------

    send(subject,text,sender,mail_to)

@shared_task
def say_hello():
    return "Hello! -- Up\'s i did it again!"

