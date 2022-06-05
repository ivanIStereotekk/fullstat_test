
from django.db import models

class Request_JSONB_Model(models.Model):
    """
    JSONB Model for savig Outer Data from request
    """
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name='Recorded Time')
    payload = models.JSONField(null=True,verbose_name='Payload')
    def __str__(self):
        return str(self.pk)
