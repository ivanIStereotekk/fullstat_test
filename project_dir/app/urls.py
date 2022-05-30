
from django.urls import path
from .views import*

from rest_framework import routers
'''Class - SimpleRouter - and Registred_Routes'''
router = routers.SimpleRouter()

'''Registred routes
--http://127.0.0.1:8000/persons/...int
--http://127.0.0.1:8000/link/
--http://127.0.0.1:8000/bookmark/
--http://127.0.0.1:8000/posts/


'''

router.register(r'persons',Person_View_Set_Api)
router.register(r'posts',Post_View_Set_Api)
router.register(r'bookmarks',Bookmark_View_Set_Api)
router.register(r'links',Link_View_Set_Api)




'''URLS'''
urlpatterns = [
    path('index/',index),
    path('detail/<str:post_slug>/',post_by_slug,name='post'),
    path('subscriptions/<int:pk>/',bookmark_by_user_id,name='subscriptions'),
    path('author/<int:pk>/',post_by_author_id,name='author_posts')
    ]
urlpatterns += router.urls