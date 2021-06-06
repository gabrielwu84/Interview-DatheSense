from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class TestSetUp(APITestCase):

    def setUp(self):
        self.registerUrl=reverse('account_api:register')
        self.loginUrl=reverse('account_api:login')
        self.uploadUrl=reverse('fileutils_api:upload')
        self.listUrl=reverse('fileutils_api:list')
        self.user_data = {
            'username': 'admin1',
            'password': 'admin1',
            'password2': 'admin1'
        }
        self.client.login(username='admin1', password='admin1')
        
        self.posFile='tests/samples/sample1.txt'
        self.negFile='tests/samples/sample4.md'

        return super().setUp()

    def tearDown(self):
        return super().tearDown()