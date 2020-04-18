from random import random
from oregon.utilities.user_prompts import ask_numeric
from oregon.utilities.shoot import shoot
from .dying import dying


# The convoluted original logic for a rider attack: RND(0)*10>((M/100-4)^2+72)/((M/100-4)^2+12)-1
def do_riders_attack(track):
    return (random() * 10) > (((float(track.mileage) / 100.0 - 4) ** 2 + 72) /
                              ((float(track.mileage) / 100.0 - 4) ** 2 + 12) - 1)


def riders_attack(inv, track, turn_state):
    peaceful = True
    if random() < 0.8:
        print("RIDERS AHEAD.  THEY DON'T LOOK HOSTILE")
    else:
        print("RIDERS AHEAD.  THEY LOOK HOSTILE")
        peaceful = False

    # riders may randomly switch sides
    if random() <= 0.2:
        peaceful = not peaceful

    print("TACTICS")
    print("(1) RUN  (2) ATTACK  (3) CONTINUE  (4) CIRCLE WAGONS")
    print("IF YOU RUN YOU'LL GAIN TIME BUT WEAR DOWN YOUR OXEN")
    response = ask_numeric("IF YOU CIRCLE YOU'LL LOSE TIME", 1, 4)
    if not peaceful:
        if response == 1:  # run
            track.add_mileage(20)
            inv.misc.subtract(15)
            inv.bullets.subtract(150)
            inv.oxen.subtract(40)
        elif response == 2:  # attack
            response, entry_time = shoot(7)
            # Original bullet loss was "B=B-B1*40-80". This produces a gain in bullets
            # when response time is less than 2 seconds and small losses when the value is longer (max: 200)
            inv.bullets.subtract(entry_time * 28.57)
            if entry_time <= 1:
                print("NICE SHOOTING---YOU DROVE THEM OFF")
            elif entry_time <= 4:
                print("KINDA SLOW WITH YOUR COLT .45")
            else:
                print("LOUSY SHOT---YOU GOT KNIFED")
                print("YOU HAVE TO SEE OL' DOC BLANCHARD")
                turn_state.injured = True
        elif response == 3:  # continue
            if random() <= 0.8:
                inv.misc.subtract(15)
                inv.bullets.subtract(150)
            else:
                print("THEY DID NOT ATTACK")
                return
        else:  # circle wagons
            response, entry_time = shoot(7)
            inv.bullets.subtract((entry_time * 30) - 80)
            track.subtract_mileage(25)
            if entry_time <= 1:
                print("NICE SHOOTING---YOU DROVE THEM OFF")
            elif entry_time <= 4:
                print("KINDA SLOW WITH YOUR COLT .45")
            else:
                print("LOUSY SHOT---YOU GOT KNIFED")
                print("YOU HAVE TO SEE OL' DOC BLANCHARD")
                turn_state.injured = True
    else:  # peaceful riders
        if response == 1:  # run
            track.add_mileage(15)
            inv.oxen.subtract(10)
        elif response == 2:  # attack
            track.subtract_mileage(5)
            inv.bullets.subtract(100)
        elif response == 4:  # circle wagons
            track.subtract_mileage(20)

    if peaceful:
        print("RIDERS WERE FRIENDLY, BUT CHECK FOR POSSIBLE LOSSES")
    else:
        print("RIDERS WERE HOSTILE--CHECK FOR LOSSES")
        if inv.bullets.value < 0:
            print("YOU RAN OUT OF BULLETS AND GOT MASSACRED BY THE RIDERS")
            dying()
