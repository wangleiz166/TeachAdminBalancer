from django.test import TestCase, Client
from django.urls import reverse
from .models import Staff

class StaffListTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some staff objects for testing
        Staff.objects.create(initials='AB', first_name='John', last_name='Doe', cat='Category A')
        Staff.objects.create(initials='CD', first_name='Jane', last_name='Smith', cat='Category B')

    def test_staff_list(self):
        url = reverse('staff_list')
        response = self.client.get(url)
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        # Assert that the staff list page is rendered
        self.assertTemplateUsed(response, 'staff_list.html')
        # Assert that the staff objects are present in the page context
        self.assertQuerysetEqual(
            response.context['page_obj'],
            Staff.objects.filter(is_delete=0),
            transform=lambda x: x
        )

    def test_staff_delete(self):
        # Get the staff object to be deleted
        staff = Staff.objects.get(initials='AB')
        url = reverse('staff_delete', args=[staff.id])
        response = self.client.post(url)
        # Assert that the staff is deleted
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Staff.objects.filter(is_delete=1).count(), 1)
        self.assertRedirects(response, reverse('staff_list'))
