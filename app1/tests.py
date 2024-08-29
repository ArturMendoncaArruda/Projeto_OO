from django.test import TestCase
from .models import UserProfile

class UserProfileModelTest(TestCase):
    def setUp(self):
        UserProfile.objects.create(name="Test User", age=30)

    def test_user_profile_creation(self):
        user_profile = UserProfile.objects.get(name="Test User")
        self.assertEqual(user_profile.age, 30)

