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

from rest_framework.decorators import api_view

from rest_framework.response import Response


# Views classes and functions
def index(request):
    list = ("<h2>Registred routes:</h2>","""
<br>--http://127.0.0.1:8000/persons/...int
<br>--http://127.0.0.1:8000/link/...int
<br>--http://127.0.0.1:8000/bookmark/...int
<br>--http://127.0.0.1:8000/posts/...int

<br>latest:
<br>http://127.0.0.1:8000/latest/

<br>paginator: 
<br>http://127.0.0.1:8000/posts/?limit=4

<br>get post by description slug:
<br>http://127.0.0.1:8000/detail/my_post_name/

<br>bookmarks by user id:
<br>http://127.0.0.1:8000/user_bookmarks/3/

<br>get post by author id:
<br>http://127.0.0.1:8000/author/1/""")
    return HttpResponse(list)


# - ViewSet --PERSON

class Person_View_Set_Api(ModelViewSet):
    """
    Person ORM model ViewSet
    """
    queryset = Person.objects.all()
    serializer_class = Person_Serializer


# - ViewSet - POST
class Post_View_Set_Api(ModelViewSet):
    """
        Post ORM model ViewSet
        """
    queryset = Post.objects.all()
    serializer_class = Post_Serializer

# - ViewSet - LINK
class Link_View_Set_Api(ModelViewSet):
    """
        Link ORM model ViewSet
        """
    queryset = Link.objects.all()
    serializer_class = Link_Serializer

# - ViewSet - BOOKMARK
class Bookmark_View_Set_Api(ModelViewSet):
    """
        Bookmark ORM model ViewSet
        """
    queryset = Bookmark.objects.all()
    serializer_class = Bookmark_Serializer

# FILTERING VIEW SET's
class Latest_View_Set_Api(ModelViewSet):
    """
        Latest Post's ViewSet
        """
    queryset = Post.objects.order_by('-created_at')
    serializer_class = Post_Serializer

# ---- GET POST BY SLUG URL
class Detail_Post_View(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = Post_Serializer
    lookup_field = 'slug'

# --- GET USER'S BOOKMARK (QuerySet)

@api_view(['GET'])
def bookmark_by_user_id(request, pk):
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
def post_by_author_id(request, pk):
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


