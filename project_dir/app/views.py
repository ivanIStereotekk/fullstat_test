"""
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
"""

from .models import Person, Post, Bookmark, Link

from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import RetrieveAPIView

from .serializers import Link_Serializer, \
    Person_Serializer, \
    Post_Serializer, \
    Bookmark_Serializer, \
    Post_Detail_Serializer

from django.http import HttpResponse, Http404

from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework.response import Response

from rest_framework.decorators import action




# Views classes and functions
def index(request):
    hello = "<h2>Go to swagger url : </h2> - http://127.0.0.1:8000/swagger/ !"
    return HttpResponse(hello)


# - ViewSet --PERSON
#@permission_classes((IsAuthenticated,))
'''class Person_View_Set_Api(ModelViewSet):
    """
    Person ORM model ViewSet
    """
    queryset = Person.objects.all()
    serializer_class = Person_Serializer
'''


# - ViewSet - POST
@permission_classes((IsAuthenticated,))
class Post_View_Set_Api(ModelViewSet):
    """
        Post ORM model ViewSet
        """
    queryset = Post.objects.all()
    serializer_class = Post_Serializer

@permission_classes((IsAuthenticated,))
class Post_Detail_View_Api(ModelViewSet):
    """
        Post ORM model ViewSet
        """
    queryset = Post.objects.all()
    serializer_class = Post_Detail_Serializer


# - ViewSet - LINK
@permission_classes((IsAuthenticated,))
class Link_View_Set_Api(ModelViewSet):
    """
        Link ORM model ViewSet
        """
    queryset = Link.objects.all()
    serializer_class = Link_Serializer

# - ViewSet - BOOKMARK
@permission_classes((IsAuthenticated,))
class Bookmark_View_Set_Api(ModelViewSet):
    """
        Bookmark ORM model ViewSet
        """
    queryset = Bookmark.objects.all()
    serializer_class = Bookmark_Serializer

# FILTERING VIEW SET's
@permission_classes((AllowAny,))
class Latest_View_Set_Api(ModelViewSet):
    """
        Latest Post's ViewSet
        """
    queryset = Post.objects.order_by('-created_at')
    serializer_class = Post_Serializer


# --- GET USER'S BOOKMARK (QuerySet)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def Get_Bookmark_by_Person_id(request, pk):
    """
    Get bookmark by user_pk http://127.0.0.1:8000/user_bookmarks/1/
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'GET':
        try:
            bookmark = Bookmark.objects.filter(person__pk=pk)
            if bookmark[0] is None:
                raise Http404
            serializer = Bookmark_Serializer(bookmark, many=True)
            return Response(serializer.data)
        except Exception:
            raise Http404


# GET POST'S BY - USER.ID

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def Get_Post_By_Author_id(request, pk):
    '''
    Get Queryset by author_id - http://127.0.0.1:8000/author/1/
    :param request:
    :param author_id:
    :return:
    '''
    if request.method == 'GET':
        try:
            post = Post.objects.filter(author__pk=pk)
            if post[0] is None:
                raise Http404
            serializer = Post_Serializer(post, many=True)
        except Exception:
            raise Http404
        return Response(serializer.data)

# ---- GET POST BY SLUG URL PLUS - COUNTING_READING

@permission_classes((AllowAny,))
@api_view(['GET'])
def Count_And_Slug_View(request, slug):
    """
    Get by slug (string) - http://127.0.0.1:8000/api/detail_slug/{slug}/
    :param request:
    :param increment():
    :param post_slug:
    :return:
    """
    if request.method == 'GET':
        try:
            post = Post.objects.get(slug=slug)
            serializer = Post_Serializer(post)
            post.increment()
            post.save()
            return Response(serializer.data)
        except Exception:
            raise Http404

