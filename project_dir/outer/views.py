"""
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
"""

from .serializers import JSON_Serializer


from .models import Request_JSONB_Model

from rest_framework.viewsets import ModelViewSet


class Get_JsonB_View(ModelViewSet):
    """
    JSONB ORM Viewset
    """
    queryset = Request_JSONB_Model.objects.all()
    serializer_class = JSON_Serializer
