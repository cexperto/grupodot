from rest_framework.test import APITestCase
from customUser.models import CustomUser

class TestModel(APITestCase):
    def test_creates_user(self):
        user = CustomUser.objects.get_or_create(
                {
                    	"email": "tmytest2@mail.com",
                    	"username":"tmytest2",                    	
                    	"password":"Ijhgfdsa1$"	
                }
        )
        self.assertIsInstance(user[0], CustomUser)
        self.assertFalse(user[0].is_staff)        
        self.assertEqual(user[0].email, 'tmytest2@mail.com')