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
router.register(r'links', Link_View_Set_Api)
router.register(r'latest', Latest_View_Set_Api)




#'''URLS'''
urlpatterns = [
    path('index/', index),
    path('bookmarks_autor_id/<int:pk>/', Get_Bookmark_by_Person_id,name='subscriptions'),
    path('posts_author_id/<int:pk>/', Get_Post_By_Author_id,name='author_posts'),
    path('read_counter_slug/<str:slug>/', Count_And_Slug_View,name='slug_count'),
    path('get_user_reactions/<int:pk>/', Get_Reactions_By_User_id,name='my_reactions'),


    ]
urlpatterns += router.urls



