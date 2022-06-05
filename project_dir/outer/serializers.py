'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''
from rest_framework import serializers

from .models import Request_JSONB_Model



#-----
class JSON_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Request_JSONB_Model
        fields = "__all__"
