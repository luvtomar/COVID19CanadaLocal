from django.urls import reverse
from django.test import TestCase

# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_sources_view_status_code(self):
        url = reverse('sources')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_line_chart_view_status_code(self):
        url = reverse('line_chart_json', kwargs={'current_city':'Ottawa Public Health', 'type':'cases'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
