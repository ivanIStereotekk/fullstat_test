
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from app.views import *

from rest_framework.authtoken.models import Token

class Anonimous_User_Tests_Cases(APITestCase):
    """
    The Pipeline of different test cases methods for anonimous user :
    """
    def test_create_account(self):
        url = 'http://127.0.0.1:8000/auth/users/'
        data = {'username': 'test_one','email':'test@app.com','password':'supersecrettest'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.get().username, 'test_one')
        self.assertEqual(Person.objects.get().email, 'test@app.com')
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

#-----------AUTHORIZED TESTS PART

class Authenticated_User_Test_Cases(APITestCase):
    def create_setups(self):
        post_data =  {'title': 'Title', 'discription': 'Discrition', "slug": "Test_Slug", 'content':'Test-Content','author': None, "req_count": 0}
        user_one = Person.objects.create_user(username='person_test_1',password='1q2w3e4r5t6y7u8i9o0p')
        user_one.save()
        token_user_one = Token.objects.create(user=user_one)
        user_two = Person.objects.create_user(username='two_test_person', password='1m2n3b3v3vc4x4x44dghgdh')
        user_two.save()
        token_user_two = Token.objects.create(user=user_two)
        client = APIClient()
        client.logout()
        client.force_authenticate(user=user_one, token=token_user_one)

    def test_login(self):
        url = 'http://127.0.0.1:8000/api/my_posts/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    #
    # response = self.client.post(url, data, format='json')
    # self.assertEqual(response.status_code, status.HTTP_201_CREATED)


#   data = {'title': 'Title', 'discription': 'Discrition', "slug": "Test_Slug", 'content': 'Test-Content',
#                 'author': str(client), "req_count": 0}