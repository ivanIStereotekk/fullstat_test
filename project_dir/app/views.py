from django.shortcuts import render

from django.contrib.auth.models import User

from .models import *

from rest_framework import generics
from rest_framework.viewsets import*

from .serializers import User_Serializer,Link_Serializer,Person_Serializer,Post_Serializer

from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')




#----------API' - LIST OBJECTS

class User_List_View_api(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = User_Serializer()


class User_Detail_View_api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = User_Serializer()


class User_Set_View_api(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = User_Serializer()








