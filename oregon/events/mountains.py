from random import random
from .blizzard import blizzard


def mountains(inv, track, turn_state):
    if not track.reached_mountains():
        return

    if (random() * 10) <= (9 - ((track.mileage / 100 - 15) ** 2 + 72) / ((track.mileage / 100 - 15) ** 2 + 12)):
        print("RUGGED MOUNTAINS")
        if random() <= 0.1:
            print("YOU GOT LOST---LOSE VALUABLE TIME TRYING TO FIND TRAIL!")
            track.subtract_mileage(60)
        elif random() <= 0.11:
            print("WAGON DAMAGED!---LOSE TIME AND SUPPLIES")
            track.subtract_mileage(20 + (30 * random()))
            inv.misc.subtract(5)
            inv.bullets.subtract(200)
        else:
            print("THE GOING GETS SLOW")
            track.subtract_mileage(45 + (random() / 0.02))

    # First pass evaluated at 950 miles (reached_mountains)
    if not track.cleared_south_pass:
        track.cleared_south_pass = True
        if random() < 0.8:
            blizzard(inv, track, turn_state)
        else:
            print("YOU MADE IT SAFELY THROUGH SOUTH PASS--NO SNOW")

    # Second pass (blue mountains) at 1700 miles
    if track.mileage >= 1700 and not track.cleared_blue_mountains:
        track.cleared_blue_mountains = True
        if random() < 0.7:
            blizzard(inv, track, turn_state)
