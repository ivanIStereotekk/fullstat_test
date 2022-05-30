
from .models import *


from rest_framework.viewsets import ModelViewSet

from .serializers import Link_Serializer, Person_Serializer, Post_Serializer, Bookmark_Serializer


from django.http import HttpResponse

from rest_framework.decorators import api_view

from rest_framework.response import Response

def index(request):
    return HttpResponse('hello world')



# - ViewSet --PERSON
'''
Returns Person Object
'''
class Person_View_Set_Api(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = Person_Serializer

# - ViewSet - POST
class Post_View_Set_Api(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Post_Serializer

# - ViewSet - LINK
class Link_View_Set_Api(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = Link_Serializer
# - ViewSet - BOOKMARK
class Bookmark_View_Set_Api(ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = Bookmark_Serializer

#-----------POSTS BY SLUG


@api_view(['GET'])
def post_by_slug(request,post_slug):
    '''
    Get by slug (string) - http://127.0.0.1:8000/detail/slug_adress_one/
    :param request:
    :param post_slug:
    :return:
    '''
    if request.method == 'GET':
        try:
            post = Post.objects.get(slug=post_slug)
            serializer = Post_Serializer(post)
            return Response(serializer.data)
        except:
            res = {'Empty Response':'No found such query'}
            return Response(res)

#--------GET USER'S BOOKMARK (QuerySet)
@api_view(['GET'])
def bookmark_by_user_id(request,pk):
    '''
    Get bookmark by user_pk http://127.0.0.1:8000/subscriptions/1/
    :param request:
    :param pk:
    :return:
    '''
    if request.method == 'GET':
        try:
            bookmark = Bookmark.objects.filter(person__pk=pk)
            print(bookmark)
            serializer = Bookmark_Serializer(bookmark,many=True)
            return Response(serializer.data)
        except:
            res = {'Empty Response':'No found such query'}
            return Response(res)

#--------GET POST'S BY - USER ID
@api_view(['GET'])
def post_by_author_id(request,pk):
    '''
    Get Queryset by author_id - http://127.0.0.1:8000/author/1/
    :param request:
    :param author_id:
    :return:
    '''
    if request.method == 'GET':
        try:
            post = Post.objects.filter(author__pk=pk)
            print(post)
            serializer = Post_Serializer(post,many=True)
            return Response(serializer.data)
        except:
            res = {'Empty Response':'No found such query'}
            return Response(res)















