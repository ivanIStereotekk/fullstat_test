'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''
from django.urls import path
from .views import Get_JsonB_View
from rest_framework import routers


urlpatterns = [
    path('dataset/<int:pk>/',Get_JsonB_View.as_view),
]