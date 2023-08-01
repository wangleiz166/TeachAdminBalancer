from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from user.models import Permission,Log,User

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.permission_mapping = {
            1: "Manager",
            2: "Employee",
            3: "IT Administrator",
        }
        # Create a test user with hashed password
        self.user = User.objects.create(user_name="admin", pass_word=make_password('test_password'), permission_id=1)

        # Create a Permission instance with menu_id=5 and associate it with the test user
        self.permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=6, position_id=1)
        self.user.permission_id = self.permission.id
        self.user.save()

        self.login_user()

    def login_user(self):
        # Simulate user login status
        login_data = {
            'username': 'admin',
            'password': 'test_password'
        }
        login_url = reverse('login')
        self.client.post(login_url, data=login_data)
