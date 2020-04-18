from random import random
from oregon.utilities.shoot import shoot


def hunt(inv, track):
    if inv.bullets.value < 40:
        print("TOUGH---YOU NEED MORE BULLETS TO GO HUNTING")
        return
    track.subtract_mileage(45)

    response, entry_time = shoot(7)
    # debug logging? print "User typed", response, "after", entry_time, "seconds"

    if entry_time < 1.0:
        print("RIGHT BETWEEN THE EYE'S---YOU GOT A BIG ONE!!!!")
        inv.food.add(52 + random() * 6)
        inv.bullets.subtract(10 - random() * 4)
    elif (100 * random()) < (13 * entry_time):
        print("SORRY---NO LUCK TODAY")
    else:
        print("NICE SHOT--RIGHT THROUGH THE NECK--FEAST TONIGHT!!")
        inv.food.add(48 - 2 * entry_time)
        inv.bullets.subtract(10 - 3 * entry_time)
