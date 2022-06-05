'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''
from django.urls import path
from .views import*
from rest_framework import routers

from django.views.generic import TemplateView


#'''Class - SimpleRouter - and Registred_Routes'''
router = routers.SimpleRouter()


router.register(r'persons', Person_View_Set_Api)
router.register(r'posts', Post_View_Set_Api)
router.register(r'bookmarks', Bookmark_View_Set_Api)
router.register(r'links', Link_View_Set_Api)
router.register(r'latest', Latest_View_Set_Api)



#'''URLS'''
urlpatterns = [
    path('index/', index),
    path('user_bookmarks/<int:pk>/', bookmark_by_user_id,name='subscriptions'),
    path('author/<int:pk>/', post_by_author_id,name='author_posts'),
    path('one/<str:slug>/', Detail_Post_View.as_view())


    ]
urlpatterns += router.urls



