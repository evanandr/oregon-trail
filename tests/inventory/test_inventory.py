from unittest import TestCase
from oregon.inventory.inventory import Inventory


class TestInventory(TestCase):
    def test_construction(self):
        inv = Inventory()
        self.assertEqual(inv.money, 700)
        self.assertEqual(inv.oxen.value, 0)
        self.assertEqual(inv.food.value, 0)
        self.assertEqual(inv.bullets.value, 0)
        self.assertEqual(inv.clothing.value, 0)
        self.assertEqual(inv.misc.value, 0)

    def test_spend(self):
        inv = Inventory()
        inv.spend(1)
        self.assertEqual(inv.money, 699)

    def test_spend_negative(self):
        inv = Inventory()
        inv.spend(701)
        self.assertEqual(inv.money, -1)

    def test_zeroize_negative_values(self):
        inv = Inventory()

        inv.oxen.value = -1
        inv.food.value = -1
        inv.bullets.value = -1
        inv.clothing.value = -1
        inv.misc.value = -1

        inv.zeroize_negative_values()

        self.assertEqual(inv.oxen.value, 0)
        self.assertEqual(inv.food.value, 0)
        self.assertEqual(inv.bullets.value, 0)
        self.assertEqual(inv.clothing.value, 0)
        self.assertEqual(inv.misc.value, 0)
