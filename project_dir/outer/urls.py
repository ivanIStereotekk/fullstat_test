'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''

from .views import Get_JsonB_View

from rest_framework import routers


'''Class - SimpleRouter - and Registred_Routes'''
outer_router = routers.SimpleRouter()
outer_router.register(r'payload_api',Get_JsonB_View)

"""
http://127.0.0.1:8000/outer_service/payload_api/
"""

urlpatterns = []
urlpatterns += outer_router.urls