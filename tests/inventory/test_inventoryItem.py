from unittest import TestCase
from oregon.inventory.inventory_item import InventoryItem


class TestInventoryItem(TestCase):
    def test_construction(self):
        item = InventoryItem()
        self.assertEqual(item.value, 0)

    def test_set_value(self):
        item = InventoryItem()
        item.value = 50
        self.assertEqual(item.value, 50)

    def test_add(self):
        item = InventoryItem()
        item.add(50)
        self.assertEqual(item.value, 50)

    def test_subtract(self):
        item = InventoryItem()
        item.subtract(50)
        self.assertEqual(item.value, -50)
