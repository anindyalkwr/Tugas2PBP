from django.test import TestCase, Client, override_settings
from django.urls import resolve, reverse
from whitenoise.storage import CompressedManifestStaticFilesStorage

@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
# Create your tests here.
class TestURLs(TestCase):

    def test_html_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_xml_exist(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
    
    def test_json_exist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    def test_template(self):
        response = Client().get('/mywatchlist/')
        self.assertTemplateUsed(response, 'mywatchlist.html')
        self.assertTemplateUsed(response, 'base.html')