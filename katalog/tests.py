from django.test import TestCase
from katalog.models import CatalogItem

# reference: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

class YourTestClass(TestCase):
    def setUp(self):
        self.firstItem = CatalogItem.objects.create(
            item_name = "Astrox 22 RX",
            item_price = 2000000,
            item_stock = 10,
            description = "Lightweight Power",
            rating = 9,
            item_url = "https://www.yonex.com/badminton/astrox-22-rx")

    def test_something_that_will_pass(self):
        self.assertTrue((self.firstItem.item_name == 'Astrox 22 RX'), 'item_name is wrong')

    def test_something_that_will_fail(self):
        self.assertFalse((self.firstItem.item_price == 2500000), 'item price is correct')

    def test_something(self):
        self.assertEqual(self.firstItem.item_url, "https://www.yonex.com/badminton/astrox-22-rx")
