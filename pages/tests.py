from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_page_rendering(self):
        response = self.client.get('/')
        response_rev = self.client.get(reverse('home'))
        self.assertEqual(response_rev.status_code, 200)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class SignUpPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_rendering(self):
        response = self.client.get('/users/signup/')
        response_rev = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_rev.status_code, 200)

    def test_signup_template_used(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)
