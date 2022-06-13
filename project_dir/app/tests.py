from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from app.views import *



class Anonimous_User_Tests_Cases(APITestCase):
    """
    The Pipeline of different test cases methods for anonimous user :
    """
    def test_anonimous_posts(self):
        url = 'http://127.0.0.1:8000/api/posts_anonimous/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'],None)
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
        data = {'username': 'test_one','email':'test@app.com','password':'supersecrettest'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.get().username, 'test_one')
        self.assertEqual(Person.objects.get().email, 'test@app.com')

#-----------AUTHORIZED TESTS PART

class Authenticated_User_Test_Cases(APITestCase):
    """
    No Understandable test cases, and no way to find well written docs !
    """
    def test_post_model_get(self):
        test_user = Person.objects.create(username='test_account', email='test@mail.com', password='qwedfgbnjkopoiuy54')
        test_token = Token.objects.create(user=test_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + test_token.key)
        url = 'http://127.0.0.1:8000/api/posts_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'], None)
    def test_bookmarks_model_get(self):
        test_user = Person.objects.create(username='test_account', email='test@mail.com', password='qwedfgbnjkopoiuy54',pk=1)
        test_token = Token.objects.create(user=test_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + test_token.key)
        url = 'http://127.0.0.1:8000/api/bookmarks_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'], None)
    def test_reactions_model_get(self):
        test_user = Person.objects.create(username='test_account', email='test@mail.com', password='qwedfgbnjkopoiuy54',pk=1)
        test_token = Token.objects.create(user=test_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + test_token.key)
        url = 'http://127.0.0.1:8000/api/reactions_model/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'], None)
    # def test_reactions_model_put(self):
    #     test_user = Person.objects.create(username='test_account', email='test@mail.com', password='qwedfgbnjkopoiuy54',pk=1)
    #     test_token = Token.objects.create(user=test_user)
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + test_token.key)
    #     url = 'http://127.0.0.1:8000/api/reactions_model/'
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['previous'], None)
# data = {
#             "title": "Mahal",
#             "discription": "Toro Y Moi - MAHAL (Full Album) 2022",
#             "content": "Mahal is the seventh studio album from Chaz Bear under the Toro y Moi moniker. The record spans through genres and sounds calling back to previous works while charting a new path forward in a way that only Bear can do.",
#             "slug": "https://youtu.be/I75uynYUjJs",
#             "author": 15,
#             "req_count": 'null'
#         }


