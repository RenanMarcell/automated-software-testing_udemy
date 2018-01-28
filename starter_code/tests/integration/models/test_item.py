from models.item import ItemModel
from tests.base_test import BaseTest


class TestItem(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('Test', 30.00)
            self.assertIsNone(ItemModel.find_by_name('Test'),
                              'Found an item with name {}, but expected not to'.format(item.name)
                              )
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('Test'),
                                 'Did not found an item with name {}, but expected to'.format(item.name)
                                 )
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('Test'),
                              'Found an item with name {}, but expected not to'.format(item.name)
                              )
