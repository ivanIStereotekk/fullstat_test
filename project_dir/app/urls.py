'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''
from django.urls import path
from .views import*
from rest_framework import routers


#'''Class - SimpleRouter - and Registred_Routes'''
router = routers.SimpleRouter()


#router.register(r'persons', Person_View_Set_Api)
router.register(r'posts', Post_View_Set_Api)
router.register(r'bookmarks', Bookmark_View_Set_Api)
router.register(r'reactions', Link_View_Set_Api)
router.register(r'latest', Latest_View_Set_Api)





#'''URLS'''
urlpatterns = [
    path('index/', index),
    path('bookmarks_user_id/<int:pk>/', Get_Bookmark_by_Person_id,name='subscriptions'),
    path('posts_author_id/<int:pk>/', Get_Post_By_Author_id,name='author_posts'),
    path('post_read_counter_and_get_by_slug/<str:slug>/', Count_And_Slug_View,name='slug_count'),
    path('reactions_by_user_id/<int:pk>/', Get_Reactions_By_User_id,name='my_reactions'),


    ]
urlpatterns += router.urls



