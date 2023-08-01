from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from user.models import User, Permission
from staff.models import Staff
from .models import Course, Project, AdminRole, SchoolRole, UniRole
from .views import list, project_list, adminrole_list, schoolrole_list, unirole_list
from django.utils import timezone

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.permission_mapping = {
            1: "Manager",
            2: "Employee",
            3: "IT Administrator",
        }
        # Create a test user but do not set the login status, and handle the user authentication related logic manually
        self.user = User.objects.create(user_name="admin", permission_id=1)
        self.staff = Staff.objects.create(
            initials="AB",
            first_name="Alex",
            last_name="Brown",
            cat="A",
            probation_year="2022",
            annual_availability=10,
            unadjusted_max=10,
            adjusted_max=10,
            availability_notes="Notes",
            employment_end_date=timezone.now(),
            probation_start_date=timezone.now()
        )
        
        # Create instances of Course, Project, AdminRole, SchoolRole, UniRole for testing
        self.course = Course.objects.create(
            name="Test Course",
            code="test_code",
            num_staff_allocated=0,
            est_num_students=10,
            hours=5
        )

        self.project = Project.objects.create(
            name="Test Project",
            code="test_project_code",
            num_staff_allocated=0,
            est_num_students=5,
            hours=3
        )

        self.adminrole = AdminRole.objects.create(
            name="Test AdminRole",
            num_staff_allocated=2,
            crit=1,
            hours=8
        )

        self.schoolrole = SchoolRole.objects.create(
            name="Test SchoolRole",
            crit=2,
            hours=6
        )

        self.unirole = UniRole.objects.create(
            name="Test UniRole",
            crit=3,
            hours=7
        )

    def login_user(self):
        # Simulate user login status
        session = self.client.session
        session['user_id'] = self.user.id
        session['username'] = self.user.user_name
        session.save()

    def test_list_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_adminrole_list_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_adminrole_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_schoolrole_list_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_schoolrole_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_unirole_list_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_unirole_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    

    def test_staffvModules_course_edit_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_course_edit', args=[self.course.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_project_edit_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_project_edit', args=[self.project.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_adminrole_edit_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_adminrole_edit', args=[self.adminrole.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_schoolrole_edit_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_schoolrole_edit', args=[self.schoolrole.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_unirole_edit_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_unirole_edit', args=[self.unirole.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_course_add_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_course_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_project_add_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_project_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_adminrole_add_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_adminrole_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_schoolrole_add_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_schoolrole_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_unirole_add_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_unirole_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_course_delete_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_course_del', args=[self.course.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_staffvModules_project_delete_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_project_del', args=[self.project.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_staffvModules_adminrole_delete_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_adminrole_del', args=[self.adminrole.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_staffvModules_schoolrole_delete_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_schoolrole_del', args=[self.schoolrole.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_staffvModules_unirole_delete_view(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=1, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        url = reverse('staffvModules_unirole_del', args=[self.unirole.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    
