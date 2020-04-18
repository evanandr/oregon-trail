from random import random
from .dying import dying


def illness(inv, track, turn_state):
    if (100 * random()) < (10 + (35 * turn_state.eating_state - 1)):
        print("MILD ILLNESS---MEDICINE USED")
        track.subtract_mileage(5)
        inv.misc.subtract(2)
    elif (100 * random()) < (100 - (40 / (4 ** (turn_state.eating_state - 1)))):
        print("BAD ILLNESS---MEDICINE USED")
        track.subtract_mileage(5)
        inv.misc.subtract(5)
    if inv.misc.value < 0:
        print("YOU RAN OUT MEDICAL SUPPLIES")
        message = "YOU DIED OF "
        if turn_state.injured:
            message += "INJURIES"
        else:
            message += "PNEUMONIA"
        print(message)
        dying()
