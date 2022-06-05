from django.http import HttpResponse
from rest_framework.decorators import api_view

from .serializers import JSON_Serializer


from .models import Request_JSONB_Model

from rest_framework.viewsets import ModelViewSet

import requests as req

from .tasks import send_letter,users_mail

@api_view(['GET'])
def payload_view(response):
    _request = req.get('https://jservice.io/api/random?count=1')
    new_obj = Request_JSONB_Model(payload=_request.text)
    new_obj.save()
    send_letter.delay(users_mail)
    info = ('<h2>Here is adress for JSON:</h2> <br> http://127.0.0.1:8000/outer/json/')
    return HttpResponse(str(new_obj.timestamp) + f''
                                                 f''
                                                 f'<br>payload is :<br>{new_obj.payload}')



class Get_JsonB_View(ModelViewSet):
    """
    JSONB ORM Viewset
    """
    queryset = Request_JSONB_Model.objects.all()
    serializer_class = JSON_Serializer
