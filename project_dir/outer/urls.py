'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''
from django.urls import path
from .views import Get_JsonB_View,payload_view

from rest_framework import routers
'''Class - SimpleRouter - and Registred_Routes'''


outer_router = routers.SimpleRouter()


outer_router.register(r'json',Get_JsonB_View)

"""
http://127.0.0.1:8000/outer/

http://127.0.0.1:8000/outer/json/
"""

urlpatterns = [
    path('',payload_view),
]
urlpatterns += outer_router.urls