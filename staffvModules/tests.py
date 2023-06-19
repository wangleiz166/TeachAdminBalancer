from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Course, Project, AdminRole, SchoolRole, UniRole
from .views import list, project_list, adminrole_list, schoolrole_list, unirole_list

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create sample objects for testing
        self.course = Course.objects.create(code='C001', name='Sample Course')
        self.project = Project.objects.create(code='P001', name='Sample Project')
        self.adminrole = AdminRole.objects.create(name='Admin Role')
        self.schoolrole = SchoolRole.objects.create(name='School Role')
        self.unirole = UniRole.objects.create(name='Uni Role')

        # Set up the request factory
        self.factory = RequestFactory()

    def test_list_view(self):
        url = reverse('list')
        request = self.factory.get(url)
        response = list(request)
        self.assertEqual(response.status_code, 200)

    def test_project_list_view(self):
        url = reverse('project_list')
        request = self.factory.get(url)
        response = project_list(request)
        self.assertEqual(response.status_code, 200)

    def test_adminrole_list_view(self):
        url = reverse('adminrole_list')
        request = self.factory.get(url)
        response = adminrole_list(request)
        self.assertEqual(response.status_code, 200)

    def test_schoolrole_list_view(self):
        url = reverse('schoolrole_list')
        request = self.factory.get(url)
        response = schoolrole_list(request)
        self.assertEqual(response.status_code, 200)

    def test_unirole_list_view(self):
        url = reverse('unirole_list')
        request = self.factory.get(url)
        response = unirole_list(request)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_course_edit_view(self):
        url = reverse('staffvModules_course_edit', args=[self.course.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_project_edit_view(self):
        url = reverse('staffvModules_project_edit', args=[self.project.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_adminrole_edit_view(self):
        url = reverse('staffvModules_adminrole_edit', args=[self.adminrole.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_schoolrole_edit_view(self):
        url = reverse('staffvModules_schoolrole_edit', args=[self.schoolrole.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_unirole_edit_view(self):
        url = reverse('staffvModules_unirole_edit', args=[self.unirole.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_course_add_view(self):
        url = reverse('staffvModules_course_add')
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_project_add_view(self):
        url = reverse('staffvModules_project_add')
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_adminrole_add_view(self):
        url = reverse('staffvModules_adminrole_add')
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_schoolrole_add_view(self):
        url = reverse('staffvModules_schoolrole_add')
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_unirole_add_view(self):
        url = reverse('staffvModules_unirole_add')
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_course_delete_view(self):
        url = reverse('staffvModules_course_delete', args=[self.course.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_project_delete_view(self):
        url = reverse('staffvModules_project_delete', args=[self.project.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_adminrole_delete_view(self):
        url = reverse('staffvModules_adminrole_delete', args=[self.adminrole.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_schoolrole_delete_view(self):
        url = reverse('staffvModules_schoolrole_delete', args=[self.schoolrole.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_staffvModules_unirole_delete_view(self):
        url = reverse('staffvModules_unirole_delete', args=[self.unirole.id])
        request = self.factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
