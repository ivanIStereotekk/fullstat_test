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
router.register(r'posts_model', Post_Fabrique_Api)
router.register(r'bookmarks_model', Bookmark_Fabrique_Api)
router.register(r'reactions_model', Link_Fabrique_Api)



#'''URLS'''
urlpatterns = [
    path('index/', index),
    path('posts_anonimous/',Post_Anonimous_Api.as_view(),name='posts-anonimous'),
    path('bookmarks_user_id/<int:pk>/', Get_Bookmark_by_Person_id,name='subscriptions'),
    path('post_author_id/<int:pk>/', Get_Post_By_Author_id,name='author-posts'),
    path('post_read_counter_and_get_by_slug/<str:slug>/', Count_And_Slug_View,name='slug-count'),
    path('reactions_by_user_id/<int:pk>/', Get_Reactions_By_User_id,name='my-reactions'),
    path('my_posts/',My_Posts_View.as_view(),name='my-posts'),
    path('my_bookmarks/',My_Bookmarks_View.as_view(),name='my-bookmarks'),
    path('my_reactions/',My_Reactions_View.as_view(),name='my-reactions'),


    ]
urlpatterns += router.urls



