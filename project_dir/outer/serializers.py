'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''
from rest_framework import serializers

from .models import Request_JSONB



#-----
class Request_JSON_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Request_JSONB
        fields = "__all__"
        depth = 2