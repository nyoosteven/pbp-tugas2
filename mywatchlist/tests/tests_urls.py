from django.test import TestCase, Client
from django.urls import reverse, resolve
from mywatchlist.views import show_watched, show_json, show_xml

class TestUrls(TestCase):
    def test_html_url(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_watched"))
        self.assertEquals(response.status_code, 200)

    def test_json_url(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code, 200)