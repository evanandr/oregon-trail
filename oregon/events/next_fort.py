from oregon.utilities.user_prompts import ask_numeric


def next_fort(inv, track):
    print("ENTER WHAT YOU WISH TO SPEND ON THE FOLLOWING")
    food = ask_numeric("FOOD", 0, inv.money)
    ammo = ask_numeric("AMMUNITION", 0, inv.money)
    clothing = ask_numeric("CLOTHING", 0, inv.money)
    misc = ask_numeric("MISCELLANEOUS SUPPLIES", 0, inv.money)
    total_spend = food + ammo + clothing + misc
    if inv.money < total_spend:
        print("YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN")
        return next_fort(inv, track)
    inv.spend(total_spend)
    inv.food.add(0.66 * food)
    inv.bullets.add(0.66 * ammo * 50)
    inv.clothing.add(0.66 * clothing)
    inv.misc.add(0.66*misc)
    track.subtract_mileage(45)
