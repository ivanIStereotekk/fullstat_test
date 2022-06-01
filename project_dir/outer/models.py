from django.db import models

class Request_JSONB(models.Model):
    """
    JSONB Model for savig Outer Data from request
    """
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name='Recorded Time')
    request_set = models.JSONField()

    def __str__(self):
        return self.pk
