from rest_framework import serializers
from .models import Post,Person,Bookmark,Link
from django.contrib.auth.models import User



#-----
class Post_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
#-----
class Person_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

#-----
class Bookmark_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = "__all__"

#-----
class Link_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"