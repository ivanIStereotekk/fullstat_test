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
    author = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Person.objects.all(),
    )

    class Meta:
        model = Post
        fields = ('title','discription','content','slug','author','req_count')
        depth = 5

#-----
class Person_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        depth = 3

#-----
class Bookmark_Serializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Person.objects.all(),
    )
    posts = serializers.PrimaryKeyRelatedField(many=True,queryset=Post.objects.all())

    class Meta:
        model = Bookmark
        fields = "__all__"
        #depth = 2

#-----
class Link_Serializer(serializers.ModelSerializer):
    whos_link = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Person.objects.all(),
    )
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    class Meta:
        model = Link
        fields = "__all__"
        depth = 3
class Reactions_Serializer(serializers.ModelSerializer):
    whos_link = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Person.objects.all(),
    )
    class Meta:
        model = Link
        fields = "__all__"

#----
class Post_Detail_Serializer(serializers.ModelSerializer):
    links = serializers.PrimaryKeyRelatedField(queryset=Link.objects.all())
    class Meta:
        model = Post
        fields = "__all__"
        depth = 3
