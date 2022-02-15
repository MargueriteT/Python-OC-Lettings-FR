from django.test import TestCase
from django.urls import reverse
from .models import Letting, Address


class LettingsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_lettings = 5
        for address_id in range(number_of_lettings):
            address = Address.objects.create(id=int(address_id),
                                             number=int(address_id),
                                             street='fakestreet',
                                             city=f'city{address_id}',
                                             state='fakestate',
                                             zip_code=address_id,
                                             country_iso_code=222)

            Letting.objects.create(title=f'title{address_id}',
                                   address=address)

    def test_address_model(self):
        address = Address.objects.filter(id=1).first()
        self.assertEqual(f'{address}', '1 fakestreet')

    def test_letting_model(self):
        letting = Letting.objects.filter(id=1).first()
        self.assertEqual(f'{letting}', 'title0')

    def test_view_list(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Lettings</title>')
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertTrue(len(response.context['lettings_list']) == 5)

    def test_detail_view(self):
        response = self.client.get(reverse('lettings:letting', args=[1]))
        self.assertContains(response, f'<title>title0</title>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
