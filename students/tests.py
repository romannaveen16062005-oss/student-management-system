
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

from .models import Student


class StudentManagementTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testadmin',
            password='TestPassword123'
        )

        self.client.force_login(self.user)

        self.student = Student.objects.create(
            register_number='STUTEST01',
            full_name='Test Student',
            email='teststudent@example.com',
            phone='9876543210',
            department='Computer Science',
            course='B.Sc Computer Science',
            date_of_birth=date(2004, 5, 15),
            address='Coimbatore'
        )

    def test_dashboard_loads(self):
        response = self.client.get(reverse('dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'students/dashboard.html'
        )

    def test_student_list_loads(self):
        response = self.client.get(reverse('student_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Student')

    def test_search_by_name(self):
        response = self.client.get(
            reverse('student_list'),
            {'search': 'Test Student'}
        )

        self.assertContains(response, 'Test Student')

    def test_search_by_register_number(self):
        response = self.client.get(
            reverse('student_list'),
            {'search': 'STUTEST01'}
        )

        self.assertContains(response, 'STUTEST01')

    def test_add_student(self):
        data = {
            'register_number': 'STUTEST02',
            'full_name': 'New Student',
            'email': 'newstudent@example.com',
            'phone': '9876543211',
            'department': 'Computer Science',
            'course': 'B.Sc Computer Science',
            'date_of_birth': '2003-06-15',
            'address': 'Coimbatore'
        }

        response = self.client.post(
            reverse('add_student'),
            data
        )

        self.assertRedirects(
            response,
            reverse('dashboard')
        )

        self.assertTrue(
            Student.objects.filter(
                register_number='STUTEST02'
            ).exists()
        )

    def test_edit_student(self):
        data = {
            'register_number': 'STUTEST01',
            'full_name': 'Updated Student',
            'email': 'teststudent@example.com',
            'phone': '9876543210',
            'department': 'Computer Science',
            'course': 'B.Sc Computer Science',
            'date_of_birth': '2004-05-15',
            'address': 'Coimbatore'
        }

        response = self.client.post(
            reverse('edit_student', args=[self.student.id]),
            data
        )

        self.assertRedirects(
            response,
            reverse('dashboard')
        )

        self.student.refresh_from_db()

        self.assertEqual(
            self.student.full_name,
            'Updated Student'
        )

    def test_delete_student(self):
        response = self.client.post(
            reverse('delete_student', args=[self.student.id])
        )

        self.assertRedirects(
            response,
            reverse('dashboard')
        )

        self.assertFalse(
            Student.objects.filter(
                id=self.student.id
            ).exists()
        )
