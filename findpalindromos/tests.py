from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from .palindrome import find_palindromes


class Palindrome(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('usertest', 'usertest@gmail.com', '1234')

    def test_palindrome(self):
        text = "Anita lava la tina"
        palindrome = find_palindromes(text)
        self.assertEqual(palindrome, "ava")


class EndpointPalindrome(APITestCase):
    def test_palindrome_endpoint_fail(self):        
        data = {
            "text": "12321"
        }
        response = self.client.post('/palindrome', data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    