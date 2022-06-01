
from .serializers import Request_JSON_Serializer



from .models import Request_JSONB

from rest_framework.viewsets import ModelViewSet

class Get_JsonB_View(ModelViewSet):
    """
    JSONB ORM Viewset
    """
    queryset = Request_JSONB.objects.all()
    serializer_class = Request_JSON_Serializer
