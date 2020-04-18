from oregon.inventory.inventory import Inventory
from oregon.utilities.user_prompts import ask_numeric


def initial_purchases():
    inv = Inventory()

    oxen_spend = ask_numeric("HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM", 200, 300)
    inv.spend(oxen_spend)
    food_spend = ask_numeric("HOW MUCH DO YOU WANT TO SPEND ON FOOD", 0)
    inv.spend(food_spend)
    ammunition_spend = ask_numeric("HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION", 0)
    inv.spend(ammunition_spend)
    clothing_spend = ask_numeric("HOW MUCH DO YOU WANT TO SPEND ON CLOTHING", 0)
    inv.spend(clothing_spend)
    misc_spend = ask_numeric("HOW MUCH DO YOU WANT TO SPEND ON MISCELLANEOUS SUPPLIES", 0)
    inv.spend(misc_spend)

    if inv.money < 0:
        print("YOU OVERSPENT--YOU ONLY HAD $700 TO SPEND.  BUY AGAIN")
        return initial_purchases()

    inv.oxen.value = oxen_spend
    inv.food.value = food_spend
    inv.bullets.value = 50 * ammunition_spend
    inv.clothing.value = clothing_spend
    inv.misc.value = misc_spend

    print("AFTER ALL YOUR PURCHASES, YOU NOW HAVE", inv.money, "DOLLARS LEFT")
    return inv
