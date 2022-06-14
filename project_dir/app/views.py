"""
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
"""

from .models import Person, Post, Bookmark, Link

from .serializers import Link_Serializer,Post_Serializer,Bookmark_Serializer,Reactions_Serializer

from django.http import HttpResponse, Http404

from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework.response import Response

from rest_framework import generics, viewsets

from rest_framework import filters

#       J O K E      H T M L   I N F O
def index(request):
    link = "http://127.0.0.1:8000/swagger/"
    data = f"<h2>Go to swagger url : </h2> - {link}"
    return HttpResponse(data)






#                R E A D   O N L Y    V I E W    S E T S
@permission_classes((AllowAny,))
class Post_Anonymous_Api(generics.ListAPIView):
    """
        Post for anonimous ORM model ViewSet - USE FILTER!
        """
    queryset = Post.objects.all()
    serializer_class = Post_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

@permission_classes((IsAuthenticated,))
class Post_Fabrique_Api(viewsets.ReadOnlyModelViewSet):
    """
        Fabrique - - USE FILTER!
        """
    queryset = Post.objects.all()
    serializer_class = Post_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

@permission_classes((IsAuthenticated,))
class Bookmark_Fabrique_Api(viewsets.ReadOnlyModelViewSet):
    """
        Bookmark Fabrique - - USE FILTER!
        """
    queryset = Bookmark.objects.all()
    serializer_class = Bookmark_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

@permission_classes((IsAuthenticated,))
class Link_Fabrique_Api(viewsets.ReadOnlyModelViewSet):
    """
        Link Fabrique - - USE FILTER!
        """
    queryset = Link.objects.all()
    serializer_class = Link_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

#          C R E A T E      A P I'S
@permission_classes((IsAuthenticated,))
class Post_Create_Api(generics.CreateAPIView):
    """
        Fabrique - - USE FILTER!
        """
    queryset = Post.objects.all()
    serializer_class = Post_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

@permission_classes((IsAuthenticated,))
class Bookmark_Create_Api(generics.CreateAPIView):
    """
        Bookmark Fabrique - - USE FILTER!
        """
    queryset = Bookmark.objects.all()
    serializer_class = Bookmark_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

@permission_classes((IsAuthenticated,))
class Link_Create_Api(generics.CreateAPIView):
    """
        Link Fabrique - - USE FILTER!
        """
    queryset = Link.objects.all()
    serializer_class = Link_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'


#       U S E R   V I E V   S E T S

@permission_classes((IsAuthenticated,))
class My_Posts_View(generics.ListAPIView):
    """
    Posts which written by authenticated user: - - USE FILTER!
    """
    serializer_class = Post_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__pk=user.pk)

#       M Y   B O O K M A R K S
@permission_classes((IsAuthenticated,))
class My_Bookmarks_View(generics.ListAPIView):
    """
    Bookmarks by authenticated user: - USE FILTER!
    """
    serializer_class = Bookmark_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(owner=user.pk)

#      M Y   R E A C T I O N S   or  L I N K
@permission_classes((IsAuthenticated,))
class My_Reactions_View(generics.ListAPIView):
    """
    Reactions (Link) by authenticated user: - - USE FILTER!
    """
    serializer_class = Link_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    def get_queryset(self):
        user = self.request.user
        return Link.objects.filter(whos_link=user.pk)

#       G E T   U S E R'S   B O O K M A R K (QuerySet)
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
            bookmark = Bookmark.objects.filter(owner__pk=pk)
            if bookmark[0] is None:
                raise Http404
            serializer = Bookmark_Serializer(bookmark, many=True)
            return Response(serializer.data)
        except Exception:
            raise Http404


#       G E T   P O S T'S   B Y    U S E R.I D

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



#       G E T   P O S T   B Y   S L U G   U R L   P L U S    C O U N T I N G   R E A D I N G S

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

#       G E T   U S E R   R E A C T I O N S (LINKS)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def Get_Reactions_By_User_id(request, pk):
    '''
    Get Reactions By user ID - /api/get_user_reactions/{id}/
    :param request:
    :param whos_link:
    :return:
    '''
    if request.method == 'GET':
        try:
            post = Link.objects.filter(whos_link__pk=pk)
            if post[0] is None:
                raise Http404
            serializer = Link_Serializer(post, many=True)
        except Exception:
            raise Http404
        return Response(serializer.data)



#                D E L E T E - U P D A T E - O N L Y - U S E R'S  - T H I N G
@permission_classes((IsAuthenticated,))
class Retrieve_Reaction_View(generics.RetrieveUpdateDestroyAPIView):
    """
    Users Reactions DELETE - PUT - PATCH - methods.
    """
    serializer_class = Link_Serializer
    def get_queryset(self):
        user = self.request.user
        return Link.objects.filter(whos_link=user.pk)

@permission_classes((IsAuthenticated,))
class Retrieve_Post_View(generics.RetrieveUpdateDestroyAPIView):
    """
    Users Posts DELETE - PUT - PATCH - methods.
    """
    serializer_class = Post_Serializer
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user.pk)
@permission_classes((IsAuthenticated,))
class Retrieve_Bookmark_View(generics.RetrieveUpdateDestroyAPIView):
    """
    Users Bookmark DELETE - PUT - PATCH - methods.
    """
    serializer_class = Bookmark_Serializer
    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(owner=user.pk)


#    S E A R C H   V I E W
from rest_framework import filters

@permission_classes((AllowAny,))
class Search_Posts_View(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Post_Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content','discription']