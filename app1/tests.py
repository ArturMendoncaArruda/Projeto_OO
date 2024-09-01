from django.test import TestCase
from .models import Jogo_final

class UserProfileModelTest(TestCase):
    def setUp(self):
        Jogo_final.objects.create(name="Test User", age=30)

    def test_user_profile_creation(self):
        user_profile = Jogo_final.objects.get(name="Test User")
        self.assertEqual(user_profile.age, 30)

