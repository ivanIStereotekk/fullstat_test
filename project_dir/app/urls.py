'''
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
'''
from django.urls import path
from .views import*
from rest_framework import routers
'''Class - SimpleRouter - and Registred_Routes'''
router = routers.SimpleRouter()

'''Registred routes
--http://127.0.0.1:8000/persons/...int
--http://127.0.0.1:8000/link/...int
--http://127.0.0.1:8000/bookmark/...int
--http://127.0.0.1:8000/posts/...int

latest:
http://127.0.0.1:8000/latest/

paginator: 
http://127.0.0.1:8000/posts/?limit=4

get post by description slug:
http://127.0.0.1:8000/detail/my_post_name/

bookmarks by user id:
http://127.0.0.1:8000/user_bookmarks/3/

get post by author id:
http://127.0.0.1:8000/author/1/

'''

router.register(r'persons',Person_View_Set_Api)
router.register(r'posts',Post_View_Set_Api)
router.register(r'bookmarks',Bookmark_View_Set_Api)
router.register(r'links',Link_View_Set_Api)
router.register(r'latest',Latest_View_Set_Api)


'''URLS'''
urlpatterns = [
    path('index/',index),
    path('detail/<str:post_slug>/',post_by_slug,name='post'),
    path('user_bookmarks/<int:pk>/',bookmark_by_user_id,name='subscriptions'),
    path('author/<int:pk>/',post_by_author_id,name='author_posts'),


    ]
urlpatterns += router.urls