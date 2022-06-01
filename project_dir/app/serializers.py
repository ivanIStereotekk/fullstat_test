'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''
from rest_framework import serializers

from .models import Post,Person,Bookmark,Link



#-----
class Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        depth = 3
#-----
class Person_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        depth = 3

#-----
class Bookmark_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = "__all__"
        depth = 2

#-----
class Link_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
        depth = 3

#----
class Post_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        depth = 2