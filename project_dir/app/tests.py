
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from app.views import *


class Anonimous_User_Tests_Cases(APITestCase):
    """
    The Pipeline of different test cases methods for anonimous user :
    """
    def setUp(self):
        self.client = APIClient()
    def test_anonimous_posts(self):
        url = 'http://127.0.0.1:8000/api/posts_anonimous/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'], None)

    def test_get_by_slug(self):
        url = 'http://127.0.0.1:8000/api/post_read_counter_and_get_by_slug/xxxx/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], "Not found.")

    def test_search_posts(self):
        url = 'http://127.0.0.1:8000/api/posts_search/?search=***'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], [])

    def test_get_my_posts(self):
        url = 'http://127.0.0.1:8000/api/my_posts/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_my_bookmarks(self):
        url = 'http://127.0.0.1:8000/api/my_bookmarks/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_my_reactions(self):
        url = 'http://127.0.0.1:8000/api/my_reactions/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_get_token(self):
        url = 'http://127.0.0.1:8000/api/token/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data['detail'], "Method \"GET\" not allowed.")

    def test_get_post(self):
        url = 'http://127.0.0.1:8000/api/posts_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_get_bookmarks(self):
        url = 'http://127.0.0.1:8000/api/bookmarks_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_get_reactions(self):
        url = 'http://127.0.0.1:8000/api/reactions_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_get_users(self):
        url = 'http://127.0.0.1:8000/auth/users/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_get_users_me(self):
        url = 'http://127.0.0.1:8000/auth/users/me/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_get_login(self):
        url = 'http://127.0.0.1:8000/auth/token/login/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data['detail'], "Method \"GET\" not allowed.")

    def test_get_logout(self):
        url = 'http://127.0.0.1:8000/auth/token/logout/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_create_account(self):
        url = 'http://127.0.0.1:8000/auth/users/'
        data = {'username': 'test_one', 'email': 'test@app.com', 'password': 'supersecrettest'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.get().username, 'test_one')
        self.assertEqual(Person.objects.get().email, 'test@app.com')


# -----------AUTHORIZED TESTS PART

class Authenticated_User_Test_Cases(APITestCase):
    """
    Token Authenticated user test cases!
    """

    def setUp(self):
        self.client = APIClient()
        self.test_user = Person.objects.create(username='test_account', email='test@mail.com',
                                               password='qwedfgbnjkopoiuy54')
        self.test_token = Token.objects.create(user=self.test_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_token.key)
        self.test_post = Post.objects.create(
            title='How to get token',
            discription='in some point token better then key',
            content='I\'ve had M.C. Hammer music in my head so much today thats its giving me a headache. I took 2 Tylenol, but....It can\'t touch this.',
            slug='something_like_a_slug',
            author=self.test_user,
            req_count= 0,
        )
        self.test_link = Link.objects.create(
            whos_link=self.test_user,
            post=self.test_post,
            estimation= -0,
            is_bookmarked=True,
            like=True,
            disslike=False)
        self.test_bookmark = Bookmark.objects.create(),
        self.test_post_one = Post.objects.create(slug='slug_one')
        self.test_post_two = Post.objects.create(slug='slug_two')
        self._post1 = Post.objects.create(slug='string1')
        self._post2 = Post.objects.create(slug='string2')
        self._queryset = (self._post2, self._post1)
        self._bookmark = Bookmark.objects.create(owner=self.test_user, bookmark_name="Great Thing!"
                                            )
    def test_post_model_get(self):
        url = 'http://127.0.0.1:8000/api/posts_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'], None)

    def test_bookmarks_model_get(self):
        url = 'http://127.0.0.1:8000/api/bookmarks_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'], None)

    def test_reactions_model_get(self):
        url = 'http://127.0.0.1:8000/api/reactions_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'], None)

    def test_publication_post(self):
        url = 'http://127.0.0.1:8000/api/create_post/'
        data = {
            "title": "How to get hadache",
            "discription": "in some point the ...",
            "content": "Common causes of canal pain include: API Test Cases !",
            "slug": "trying_tests",
            "author": int(self.test_user.pk),
            "req_count": 0,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['slug'],"trying_tests")
    def test_publication_bookmark(self):
        url = 'http://127.0.0.1:8000/api/create_bookmark/'
        data = {
            "owner": int(self.test_user.pk),
            "posts": [self.test_post.pk,self.test_post_one.pk,self.test_post_two.pk],
            "bookmark_name": "Hello from nowhere",
            "pk":1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['bookmark_name'], "Hello from nowhere")

    def test_publication_reaction(self):
        url = 'http://127.0.0.1:8000/api/create_reaction/'
        data = {
            "whos_link": int(self.test_user.pk),
            "post": self.test_post_one.pk,
            "estimation": -0,
            "is_bookmarked": True,
            "like": True,
            "disslike": False,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['is_bookmarked'], True )
    def test_get_my_reactions_by_id(self):
        url = f'http://127.0.0.1:8000/api/reactions_by_user_id/{self.test_user.pk}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_posts_model_pk(self):
        url = f'http://127.0.0.1:8000/api/posts_model/{self.test_post.pk}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_bookmarks_model(self):
        url = f'http://127.0.0.1:8000/api/bookmarks_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_reactions_model(self):
        url = f'http://127.0.0.1:8000/api/reactions_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_user_data(self):
        url = 'http://127.0.0.1:8000/auth/users/me/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_by_slug_counter(self):
        url = 'http://127.0.0.1:8000/api/post_read_counter_and_get_by_slug/something_like_a_slug/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_retrieve_post_get_pk(self):
        url = f'http://127.0.0.1:8000/api/retrieve_post/{self.test_post.pk}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_retrieve_bookmark_get_pk(self):
        url = f'http://127.0.0.1:8000/api/retrieve_bookmark/{self._bookmark.pk}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_retrieve_reaction_get_pk(self):
        url = f'http://127.0.0.1:8000/api/retrieve_reaction/{self.test_link.pk}'
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
######## P A T C H #################
    def test_retrieve_post_PATCH_pk(self):
        url = f'http://127.0.0.1:8000/api/retrieve_post/{self.test_post.pk}'
        data_patch = {"req_count": 10,}
        response = self.client.patch(url,data_patch, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['req_count'],10)
    def test_retrieve_bookmark_PATCH_pk(self):
        url = f'http://127.0.0.1:8000/api/retrieve_bookmark/{self._bookmark.pk}'
        data_patch = {"bookmark_name": "When you do well...)", }
        response = self.client.patch(url,data_patch, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bookmark_name'], "When you do well...)")
    def test_retrieve_reaction_PATCH_pk(self):
        url = f'http://127.0.0.1:8000/api/retrieve_reaction/{self.test_link.pk}'
        data_patch = {"like": False,
            "disslike": True,
        }
        response = self.client.patch(url, data_patch, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['like'], False)
        self.assertEqual(response.data['disslike'], True)
















