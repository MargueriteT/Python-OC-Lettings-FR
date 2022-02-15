from django.test import TestCase
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User


class ProfilesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_profiles = 5
        for profile in range(number_of_profiles):
            user = User.objects.create(id=int(profile),
                                       username=f'user{profile}',
                                       email=f'user{profile}@mail.com',
                                       first_name=f'first{profile}',
                                       last_name=f'last{profile}',
                                       password=f'password{profile}')

            Profile.objects.create(user=user,
                                   favorite_city='Paris')

    def test_profile_model(self):
        profile = Profile.objects.filter(user_id=1).first()
        self.assertEqual(f'{profile}', 'user1')

    def test_list_view(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Profiles</title>')
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertTrue(len(response.context['profiles_list']) == 5)

    def test_details_view(self):
        response = self.client.get(reverse('profiles:profile', args=['user1']))
        self.assertContains(response, f'<title>user1</title>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
