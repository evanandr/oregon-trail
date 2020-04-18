from random import random
from .illness import illness


def blizzard(inv, track, turn_state):
    print("BLIZZARD IN MOUNTAIN PASS--TIME AND SUPPLIES LOST")
    inv.food.subtract(25)
    inv.misc.subtract(10)
    inv.bullets.subtract(300)
    track.subtract_mileage(30 + (40 * random()))
    if inv.clothing.value < (18 + (2 * random())):
        illness(inv, track, turn_state)
