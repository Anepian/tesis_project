from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Thesis

class ThesisTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.superuser = User.objects.create_superuser(username='admin', password='adminpassword')
        self.thesis = Thesis.objects.create(
            title='Test Thesis',
            author='Test Author',
            advisor='Test Advisor',
            co_advisor='Test Co-Advisor',
            year=2023,
            category='Test Category',
            summary='Test Summary',
            pdf='test.pdf',
            visible=True,
            uploaded_by=self.user
        )

    def test_visitor_can_view_theses(self):
        response = self.client.get(reverse('tesis:visitor_view_theses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Thesis')

    def test_authenticated_user_can_upload_thesis(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('tesis:upload_thesis'), {
            'title': 'New Thesis',
            'author': 'New Author',
            'advisor': 'New Advisor',
            'co_advisor': 'New Co-Advisor',
            'year': 2023,
            'category': 'New Category',
            'summary': 'New Summary',
            'pdf': 'new.pdf',
            'visible': True
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful upload
        self.assertTrue(Thesis.objects.filter(title='New Thesis').exists())

    def test_superuser_can_view_all_theses(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('tesis:upload_thesis'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Thesis')

    def test_user_registration_with_security_key(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'security_key': 'admin123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_registration_with_invalid_security_key(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'security_key': 'wrongkey'
        })
        self.assertEqual(response.status_code, 200)  # Stay on the same page
        self.assertFalse(User.objects.filter(username='newuser').exists())
        self.assertContains(response, 'Clave de seguridad incorrecta.')