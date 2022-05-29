
from .models import *


from rest_framework.viewsets import ModelViewSet,ViewSetMixin

from .serializers import Link_Serializer, Person_Serializer, Post_Serializer, Bookmark_Serializer

from django.http import HttpResponse,JsonResponse,request

def index(request):
    return HttpResponse('hello world')



# - ViewSet --PERSON
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

#-----------











