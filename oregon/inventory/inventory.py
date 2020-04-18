from .inventory_item import InventoryItem


class Inventory(object):
    @property
    def money(self):
        return self._money

    def spend(self, cost):
        self._money -= int(cost)

    def print_warnings(self):
        if self.food.value < 12:
            print("YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!")

    def print_inventory(self):
        print('{0:8}|{1:9}|{2:10}|{3:14}|{4:6}|'.format("FOOD", " BULLETS ", " CLOTHING ", " MISC. SUPP. ", " CASH "))
        print('{0:7} |{1:8} |{2:9} |{3:13} |{4:5} |'.format(self.food.value, self.bullets.value, self.clothing.value,
                                                            self.misc.value, self._money))

    def zeroize_negative_values(self):
        if self.oxen.value < 0:
            self.oxen.value = 0
        if self.food.value < 0:
            self.food.value = 0
        if self.bullets.value < 0:
            self.bullets.value = 0
        if self.clothing.value < 0:
            self.clothing.value = 0
        if self.misc.value < 0:
            self.misc.value = 0

    def __init__(self):
        self._money = 700
        self.oxen = InventoryItem()
        self.food = InventoryItem()
        self.bullets = InventoryItem()
        self.clothing = InventoryItem()
        self.misc = InventoryItem()
