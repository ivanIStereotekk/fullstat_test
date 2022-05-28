from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import*


router = DefaultRouter()

router.register('users',User_Set_View_api)


urlpatterns = [
    path('index/',index),
    path('api/',include(router.urls)),


    ]