from unittest import TestCase
from oregon import Inventory


class TestInventory(TestCase):
    def test_construction(self):
        inv = Inventory()
        self.assertEquals(inv.money, 700)
        self.assertEquals(inv.oxen.value, 0)
        self.assertEquals(inv.food.value, 0)
        self.assertEquals(inv.bullets.value, 0)
        self.assertEquals(inv.clothing.value, 0)
        self.assertEquals(inv.misc.value, 0)

    def test_spend(self):
        inv = Inventory()
        inv.spend(1)
        self.assertEquals(inv.money, 699)

    def test_spend_negative(self):
        inv = Inventory()
        inv.spend(701)
        self.assertEquals(inv.money, -1)

    def test_zeroize_negative_values(self):
        inv = Inventory()

        inv.oxen.value = -1
        inv.food.value = -1
        inv.bullets.value = -1
        inv.clothing.value = -1
        inv.misc.value = -1

        inv.zeroize_negative_values()

        self.assertEquals(inv.oxen.value, 0)
        self.assertEquals(inv.food.value, 0)
        self.assertEquals(inv.bullets.value, 0)
        self.assertEquals(inv.clothing.value, 0)
        self.assertEquals(inv.misc.value, 0)
