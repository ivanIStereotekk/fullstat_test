from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory, force_authenticate
from app.models import Person,Post
from app.views import *

class Anonimous_User_Tests_Cases(APITestCase):
    """
    The Pipeline of different test cases methods are here :
    """
    def test_create_account(self):
        url = 'http://127.0.0.1:8000/auth/users/'
        data = {'username': 'test_one','email':'test@app.com','password':'supersecrettest'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.get().username, 'test_one')
        self.assertEqual(Person.objects.get().email, 'test@app.com')
    def test_get_latest_posts(self):
        url = 'http://127.0.0.1:8000/api/latest/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['previous'],None)
    def test_create_post(self):
        url = 'http://127.0.0.1:8000/api/latest/'
        data = {'title': 'Title', 'discription': 'Discrition', "slug": "Test_Slug", 'content': 'Test-Content','author': None, "req_count": 0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


#   data = {'title': 'Title', 'discription': 'Discrition', "slug": "Test_Slug", 'content': 'Test-Content',
#                 'author': str(client), "req_count": 0}