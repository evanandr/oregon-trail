from time import sleep
from random import random
from .illness import illness
from .dying import dying
from oregon.utilities.shoot import shoot


def turn_event_selection(inv, track, turn_state):
    option = 0
    ranges = [6, 11, 13, 15, 17, 22, 32, 35, 37, 42, 44, 54, 64, 69, 95]
    random_number = 100 * random()
    for value in ranges:
        if random_number <= value:
            break
        option += 1

    if option == 0:  # wagon breaks down
        print("WAGON BREAKS DOWN--LOSE TIME AND SUPPLIES FIXING IT")
        track.subtract_mileage(15 + 5 * random())
        inv.misc.subtract(8)
        sleep(1)
    elif option == 1:  # ox injure leg
        print("OX INJURES LEG---SLOWS YOU DOWN REST OF TRIP")
        track.subtract_mileage(25)
        inv.oxen.subtract(20)
        sleep(1)
    elif option == 2:  # daughter breaks arm
        print("BAD LUCK---YOUR DAUGHTER BROKE HER ARM")
        print("YOU HAD TO STOP AND USE SUPPLIES TO MAKE A SLING")
        track.subtract_mileage(5 + 4 * random())
        inv.misc.subtract(2 + 3 * random())
        sleep(1)
    elif option == 3:  # ox wanders off
        print("OX WANDERS OFF---SPEND TIME LOOKING FOR IT")
        track.subtract_mileage(17)
        sleep(1)
    elif option == 4:  # son gets lost
        print("YOUR SON GETS LOST---SPEND HALF THE DAY LOOKING FOR HIM")
        track.subtract_mileage(10)
        sleep(1)
    elif option == 5:  # unsafe water
        print("UNSAFE WATER--LOSE TIME LOOKING FOR CLEAN SPRING")
        track.subtract_mileage((10 * random()) + 2)
        sleep(1)
    elif option == 6:  # heavy rains (mountains only)
        if track.reached_mountains():
            print("HEAVY RAINS---TIME AND SUPPLIES LOST")
            inv.food.subtract(10)
            inv.bullets.subtract(500)
            inv.misc.subtract(15)
            track.subtract_mileage((10 * random()) + 5)
            sleep(1)
    elif option == 7:  # bandits attack
        print("BANDITS ATTACK")
        sleep(1)
        response, entry_time = shoot(7)
        inv.bullets.subtract(20 * entry_time)
        if inv.bullets.value <= 0:
            print("YOU RAN OUT OF BULLETS---THEY GET LOTS OF CASH")
            inv.spend(inv.money * 0.66)
        elif entry_time <= 1:
            print("QUICKEST DRAW OUTSIDE OF DODGE CITY!!!")
            print("YOU GOT 'EM!")
        else:
            print("YOU GOT SHOT IN THE LEG AND THEY TOOK ONE OF YOUR OXEN")
            print("BETTER HAVE A DOC LOOK AT YOUR WOUND")
            turn_state.injured = True
            inv.misc.subtract(5)
            inv.oxen.subtract(20)
    elif option == 8:  # fire in the wagon
        print("THERE WAS A FIRE IN YOUR WAGON--FOOD AND SUPPLIES DAMAGED")
        inv.food.subtract(40)
        inv.bullets.subtract(400)
        inv.misc.subtract((random()*8) + 3)
        track.subtract_mileage(15)
        sleep(1)
    elif option == 9:  # heavy fog
        print("LOSE YOUR WAY IN HEAVY FOG---TIME IS LOST")
        track.subtract_mileage(10 + (5 * random()))
        sleep(1)
    elif option == 10:  # poisonous snake
        print("YOU KILLED A POISONOUS SNAKE AFTER IT BIT YOU")
        inv.bullets.subtract(10)
        inv.misc.subtract(5)
        sleep(1)
        if inv.misc.value <= 0:
            print("YOU DIE OF SNAKEBITE SINCE YOU HAVE NO MEDICINE")
            dying()
    elif option == 11:  # wagon swamped fording river
        print("WAGON GETS SWAMPED FORDING RIVER--LOSE FOOD AND CLOTHES")
        inv.food.subtract(30)
        inv.clothing.subtract(20)
        track.subtract_mileage(20 + (20 * random()))
        sleep(1)
    elif option == 12:  # wild animals attack
        print("WILD ANIMALS ATTACK!")
        sleep(1)
        response, entry_time = shoot(7)
        if inv.bullets.value < 40:
            print("YOU WERE TOO LOW ON BULLETS--")
            print("THE WOLVES OVERPOWERED YOU")
            turn_state.injured = True
        if entry_time <= 2:
            print("NICE SHOOTIN' PARDNER---THEY DIDN'T GET MUCH")
        else:
            print("SLOW ON THE DRAW---THEY GOT AT YOUR FOOD AND CLOTHES")
        inv.bullets.subtract(20 * entry_time)
        inv.clothing.subtract(4 * entry_time)
        inv.food.subtract(8 * entry_time)
    elif option == 13:  # cold weather
        message = "COLD WEATHER---BRRRRRRR!---YOU "
        insufficient_clothing = False
        if inv.clothing.value < (22 + (4 * random())):
            message += "DON'T "
            insufficient_clothing = True
        message += "HAVE ENOUGH CLOTHING TO KEEP YOU WARM"
        print(message)
        sleep(1)
        if insufficient_clothing:
            illness(inv, track, turn_state)
    elif option == 14:  # hail storm
        print("HAIL STORM---SUPPLIES DAMAGED")
        track.subtract_mileage(5 + (10 * random()))
        inv.bullets.subtract(200)
        inv.misc.subtract(4 + (3 * random()))
        sleep(1)
    elif option == 15:  # illness (based on eating choice)
        if turn_state.eating_poorly():
            illness(inv, track, turn_state)
        elif turn_state.eating_moderately() and random() > 0.25:
            illness(inv, track, turn_state)
        elif turn_state.eating_well() and random() < 0.5:
            illness(inv, track, turn_state)
        sleep(1)
    else:  # helpful indians
        print("HELPFUL INDIANS SHOW YOU WHERE TO FIND MORE FOOD")
        inv.food.add(14)
        sleep(1)
