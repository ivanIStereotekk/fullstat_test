from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import*

'''Classes - DefaultRouter - and Registred_Routers'''
person_router = DefaultRouter()
post_router = DefaultRouter()
link_router = DefaultRouter()
bookmark_router = DefaultRouter()
'''Registred'''
person_router.register('person',Person_View_Set_Api)
post_router.register('posts',Post_View_Set_Api)
link_router.register('links',Link_View_Set_Api)
bookmark_router.register('bookmark',Bookmark_View_Set_Api)

'''URLS'''
urlpatterns = [
    path('index/',index),
    path('api/',include(person_router.urls)),
    path('api/',include(post_router.urls)),
    path('api/',include(link_router.urls)),
    path('api/',include(bookmark_router.urls)),
    ]