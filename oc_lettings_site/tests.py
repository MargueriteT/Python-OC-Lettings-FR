from django.test import TestCase
from django.urls import reverse


class LettingsViewTest(TestCase):
    def test_view_list(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Holiday Homes</title>')
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
