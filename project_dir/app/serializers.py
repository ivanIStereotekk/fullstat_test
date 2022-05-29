from django.db.models import QuerySet
from rest_framework import serializers
from .models import Post,Person,Bookmark,Link,Manager_Set
from django.db import models


#-----
class Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
#-----
class Person_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

#-----
class Bookmark_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = "__all__"

#-----
class Link_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

class Manager_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Manager_Set
        fields = "__all__"