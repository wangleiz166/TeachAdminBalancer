from django.test import TestCase, Client
from django.urls import reverse
from user.models import User, Permission
from staff.models import Staff
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import date

class StaffViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
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

    def login_user(self):
        # Simulate user login status
        session = self.client.session
        session['user_id'] = self.user.id
        session['username'] = self.user.user_name
        session.save()

    def test_staff_list_authenticated_user_with_permission(self):
        # Add permissions for users to access the staff list
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=2, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        # Create a request using Client
        url = reverse('staff_list')  # Replace with the URL name of the staff_list view
        response = self.client.get(url)

        # Assert that the user successfully accessed the staff list
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff_list.html')

    def test_staff_detail_authenticated_user_with_permission(self):
        # Add permissions for users to access the staff detail
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=2, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()

        # Setting the user login status
        self.login_user()

        # Create a request using Client
        url = reverse('staff_detail', kwargs={'staffId': self.staff.id})  # Replace with the URL name of the staff_detail view
        response = self.client.get(url)

        # Assert that the user successfully accessed the staff detail
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff_detail.html')

    # Continue this way to create tests for staff_delete, staff_add, and staff_update views.

    def test_staff_delete(self):
        # Mock a logged in user by setting a session value
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=2, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()
        
        # Setting the user login status
        self.login_user()

        response = self.client.get(reverse('staff_delete', kwargs={'staffId': self.staff.id}))
        self.assertEqual(response.status_code, 302)  # The request should be redirected
        # The staff instance should be marked as deleted
        self.assertEqual(Staff.objects.get(id=self.staff.id).is_delete, 1)

    def test_staff_add(self):
        # Mock a logged in user by setting a session value
        permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=2, position_id=1)
        self.user.permission_id = permission.id
        self.user.save()
        
        # Setting the user login status
        self.login_user()

        # Define the url and data to be posted
        url = reverse('staff_add')
        data = {
            'initials': 'test',
            'firstName': 'test',
            'lastName': 'test',
            'cat': 'some value',
            'probation': '2022',  # Changed this key to 'probation' to match the business logic
            'availability': '10',  # Assuming 'annual_availability' is retrieved by 'availability'
            'unadjustedMax': '10',  # Assuming 'unadjusted_max' is retrieved by 'unadjustedMax'
            'adjustedMax': '10',  # Assuming 'adjusted_max' is retrieved by 'adjustedMax'
            'availabilityNotes': "Notes",  # Assuming 'availability_notes' is retrieved by 'availabilityNotes'
            'emplEndDate': timezone.now().strftime('%Y-%m-%d'),  # Convert the date to a string
            'probationStartDate': timezone.now().strftime('%Y-%m-%d'),  # Convert the date to a string
            'probationStartYearStage': 'Stage 1',

        }

        # Make a POST request
        response = self.client.post(url, data)

        # Check if the status code is 302 (which denotes a successful POST operation and a redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the staff is added in the database
        self.assertTrue(Staff.objects.filter(initials='test').exists())


def test_staff_update(self):
    # Mock a logged in user by setting a session value
    permission = Permission.objects.create(user_id=self.user.id, permission="Manager", menu_id=2, position_id=1)
    self.user.permission_id = permission.id
    self.user.save()

    # Setting the user login status
    self.login_user()

    # Create a staff object to update
    staff_to_update = Staff.objects.create(
        initials='initials',
        first_name='firstName',
        last_name='lastName',
        cat='cat',
        probation_year=2022,
        annual_availability=10,
        unadjusted_max=10,
        adjusted_max=10,
        availability_notes="availabilityNotes",
        employment_end_date=date.today(),
        probation_start_date=date.today(),
        probation_start_year_stage='Stage 1'
    )

    # Define the url and data to be posted
    url = reverse('staff_update', args=[staff_to_update.id])  
    data = {
        'initials': 'updated_initials',
        'firstName': 'updated_firstName',
        'lastName': 'updated_lastName',
        'cat': 'updated_cat',
        'probation': '2023',
        'availability': '20',
        'unadjustedMax': '20',
        'adjustedMax': '20',
        'availabilityNotes': "updated_availabilityNotes",
        'emplEndDate': date.today(),  
        'probationStartDate': date.today(),  
        'probationStartYearStage': 'Stage 2',
    }

    # Make a POST request
    response = self.client.post(url, data)

    # Check if the status code is 302 (which denotes a successful POST operation and a redirect)
    self.assertEqual(response.status_code, 302)

    # Check if the staff is updated in the database
    updated_staff = Staff.objects.get(id=staff_to_update.id)
    self.assertEqual(updated_staff.initials, 'updated_initials')
    self.assertEqual(updated_staff.first_name, 'updated_firstName')
    self.assertEqual(updated_staff.last_name, 'updated_lastName')
    # ... and so on for all fields


    

