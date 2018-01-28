from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        i = ItemModel('Test', 30.00)

        self.assertEqual(i.name, 'Test', "The name of the item creation does not match the constructor argument")
        self.assertEqual(i.price, 30.00, "The price of the item creation does not match the constructor argument")

    def test_json(self):
        i = ItemModel('Test', 30.00)

        self.assertEqual(i.json(), {'name': 'Test', 'price': 30.00})
