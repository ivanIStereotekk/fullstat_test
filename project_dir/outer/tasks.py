# Create your tasks here


from project_dir.celery import app
from outer.mailer import send,users_mail
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)



@app.task
def send_letter():
    send(users_mail)



@shared_task
def say_hello():
    return "hello world"