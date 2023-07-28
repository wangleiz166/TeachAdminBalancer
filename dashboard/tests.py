from django.test import TestCase, Client
from django.urls import reverse
from user.models import User, Permission
from dashboard.views import dashboard

class DashboardViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.permission_mapping = {
            1: "Manager",
            2: "Employee",
            3: "IT Administrator",
        }
        # Create a test user but do not set the login status, and handle the user authentication related logic manually
        self.user = User.objects.create(user_name="admin", permission_id=1)

    def login_user(self):
        # Simulate user login status
        session = self.client.session
        session['user_id'] = self.user.id
        session['username'] = self.user.user_name
        session.save()

    def test_dashboard_authenticated_user_with_permission(self):
        # Add permissions for users to access the dashboard
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=4, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Create a request using Client
        url = reverse('dashboard')  # Replace with the URL name of the dashboard view
        # Setting the user login status
        self.login_user()

        response = self.client.get(url)

        
        # Assert that the user successfully accessed the dashboard
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_dashboard_authenticated_user_without_permission(self):
        # Do not add permission for users to access the dashboard
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=4, position_id=0)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        # Create a request using Client
        url = reverse('dashboard')  # Replace with the URL name of the dashboard view
        response = self.client.get(url)

        # Assert that the user is redirected to a warning page
        self.assertRedirects(response, '/setting/warn', fetch_redirect_response=False)  # Replace with the URL of the warning page