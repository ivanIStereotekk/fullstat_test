#from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase #APIClient, APIRequestFactory, force_authenticate
#from app.models import Person,Post
from app.views import *

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


# class Logged_User_Test_Cases(APITestCase):
#     """
#     The Pipeline of different test cases for registred user:
#     """



        # data = {'title': 'Title', 'discription': 'Discrition', "slug": "Test_Slug", 'content': 'Test-Content','author': None, "req_count": 0}
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)


#   data = {'title': 'Title', 'discription': 'Discrition', "slug": "Test_Slug", 'content': 'Test-Content',
#                 'author': str(client), "req_count": 0}