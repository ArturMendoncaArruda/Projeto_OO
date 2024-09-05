from django.test import TestCase
from .models import Dados_jogo

class UserProfileModelTest(TestCase):
    def setUp(self):
        Dados_jogo.objects.create(name="Test User", age=30)

    def test_user_profile_creation(self):
        user_profile = Dados_jogo.objects.get(name="Test User")
        self.assertEqual(user_profile.age, 30)

