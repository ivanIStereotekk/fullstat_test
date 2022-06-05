import os

from celery import Celery


from celery.schedules import crontab

#   pip install -U "celery[redis]"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_dir.settings')


app = Celery('project_dir')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


