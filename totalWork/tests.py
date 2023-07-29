from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from staffvModules.models import TeachCourse, TeachProject, TeachAdminRole, TeachSchoolRoles, TeachUniRoles
from user.models import Log,User,Permission
from django.utils import timezone
from . import views


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.permission_mapping = {
            1: "Manager",
            2: "Employee",
            3: "IT Administrator",
        }
        # Create a test user with permission for testing purposes
        self.user = User.objects.create(user_name="admin", permission_id=1)

    def login_user(self):
        # Simulate user login status
        session = self.client.session
        session['user_id'] = self.user.id
        session['username'] = self.user.user_name
        session.save()

    def test_total_work_list(self):
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=3, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('total_work_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for success
        # ... (Add more assertions to check the data displayed on the page)


    def test_admin_roles(self):
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=3, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('admin_roles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for success
        # ... (Add more assertions to check the data displayed on the page)

    def test_download_admin_roles(self):
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=3, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('download_admin_roles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for success
        # ... (Add more assertions to check the CSV content in the response)

    def test_overall_calcs(self):
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=3, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('overall_calcs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for success
        # ... (Add more assertions to check the data displayed on the page)

    def test_download_overall_calcs(self):
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=3, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('download_overall_calcs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for success
        # ... (Add more assertions to check the CSV content in the response)

    def test_frozen_modules(self):
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=3, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('frozen_modules')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for success
        # ... (Add more assertions to check the data displayed on the page)

    # Add more test methods for other views if needed
