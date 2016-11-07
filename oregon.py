#!/usr/bin/python
from datetime import date
from datetime import timedelta
from random import random
from sys import stdout
from time import time
from msvcrt import kbhit, getche


class TripTracker:
    def random_advance(self, oxen):
        self.mileage += 200 + (oxen - 220) / 5 + 10 * random()
        self.mileage = int(self.mileage)
        # LET M = M + 200 + (A - 220) / 5 + 10 * RND(0)

    def subtract_mileage(self, lost_ground):
        self.mileage -= lost_ground
        if self.mileage < 0:
            self.mileage = 0

    def print_mileage(self):
        print "TOTAL MILEAGE IS", self.mileage

    def __init__(self):
        self.mileage = 0


# The DOW and year will be hardcoded, we advance two
# weeks through Mondays between March 39th and November 22nd
class Calendar:
    def advance_date(self):
        self.date += timedelta(days=14)
        self.turn_count += 1

    def print_date(self):
        print ""
        print self.date.strftime("Monday %B %d 1847")
        print ""

    def is_final_turn(self):
        if self.turn_count == 19:
            return True
        else:
            return False

    def __init__(self):
        self.date = date(2016, 3, 29)
        self.turn_count = 1


# Do not allow values to go below zero
class Inventory:

    def spend(self, cost):
        self.money -= cost

    def get_money(self):
        return self.money

    def set_oxen(self, oxen_spend):
        self.oxen = int(oxen_spend)

    def get_oxen(self):
        return self.oxen

    def set_food(self, food_spend):
        self.food = int(food_spend)

    def get_food(self):
        return self.food

    def add_food(self, food):
        self.food += int(food)

    def subtract_food(self, food):
        self.food -= int(food)

    def set_bullets(self, bullet_spend):
        self.ammunition = int(50 * bullet_spend)
        self.bullets = int(bullet_spend)

    def get_bullets(self):
        return self.ammunition

    def add_bullets(self, ammo):
        self.ammunition += int(ammo)

    def subtract_bullets(self, ammo):
        self.ammunition -= int(ammo)

    def set_clothing(self, clothing_spend):
        self.clothing = int(clothing_spend)

    def get_clothing(self):
        return self.clothing

    def set_misc(self, misc_spend):
        self.misc = misc_spend

    def get_misc(self):
        return self.misc

    def print_warnings(self):
        if self.food < 12:
            print "YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!"

    def print_inventory(self):
        print '{0:8}|{1:9}|{2:10}|{3:14}|{4:6}|'.format("FOOD", " BULLETS ", " CLOTHING ", " MISC. SUPP. ", " CASH ")
        print '{0:7} |{1:8} |{2:9} |{3:13} |{4:5} |'.format(self.food, self.ammunition, self.clothing,
                                                            self.misc, self.money)

    def __init__(self):
        self.money = 700
        self.oxen = 0
        self.food = 0
        self.ammunition = 0
        self.bullets = 0
        self.clothing = 0
        self.misc = 0


def print_instructions():
    print "Instructions!"
    print "THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM"
    print "INDEPENDENCE, MISSOURI TO OREGON CITY, OREGON IN 1847."
    print "YOUR FAMILY OF FIVE WILL COVER THE 2000 MILE OREGON TRAIL"
    print "IN 5-6 MONTHS --- IF YOU MAKE IT ALIVE."
    print
    print "YOU HAD SAVED $900 TO SPEND FOR THE TRIP, AND YOU'VE JUST"
    print "   PAID $200 FOR A WAGON."
    print "YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE"
    print "   FOLLOWING ITEMS:"
    print
    print "     OXEN - YOU CAN SPEND $200-$300 ON YOUR TEAM"
    print "            THE MORE YOU SPEND, THE FASTER YOU'LL GO"
    print "               BECAUSE YOU'LL HAVE BETTER ANIMALS"
    print
    print "     FOOD - THE MORE YOU HAVE, THE LESS CHANCE THERE"
    print "               IS OF GETTING SICK"
    print
    print "     AMMUNITION - $1 BUYS A BELT OF 50 BULLETS"
    print "            YOU WILL NEED BULLETS FOR ATTACKS BY ANIMALS"
    print "               AND BANDITS, AND FOR HUNTING FOOD"
    print
    print "     CLOTHING - THIS IS ESPECIALLY IMPORTANT FOR THE COLD"
    print "               WEATHER YOU WILL ENCOUNTER WHEN CROSSING"
    print "               THE MOUNTAINS"
    print
    print "     MISCELLANEOUS SUPPLIES - THIS INCLUDES MEDICINE AND"
    print "               OTHER THINGS YOU WILL NEED FOR SICKNESS"
    print "               AND EMERGENCY REPAIRS"
    print ""
    print ""
    print "YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -"
    print "OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG"
    print "THE WAY WHEN YOU RUN LOW.  HOWEVER, ITEMS COST MORE AT"
    print "THE FORTS.  YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET"
    print "MORE FOOD."
    print "WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,"
    print "YOU WILL SEE THE WORDS: TYPE BANG.  THE FASTER YOU TYPE"
    print "IN THE WORD 'BANG' AND HIT THE 'RETURN' KEY, THE BETTER"
    print "LUCK YOU'LL HAVE WITH YOUR GUN."
    print
    print "WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A '$'."
    print
    print "GOOD LUCK!!!"


def ask_yes_no(prompt):
    prompt += " "
    response = str(raw_input(prompt)).lower().strip()
    if response[0] == 'y':
        return True
    if response[0] == 'n':
        return False
    else:
        return ask_yes_no(prompt)


def ask_numeric(prompt, lower_bound=None, upper_bound=None):
    if not prompt.endswith(" "):
        prompt += " "
    response = str(raw_input(prompt)).lower().strip()
    try:
        value = int(response)
    except ValueError:
        print "IMPOSSIBLE"
        return ask_numeric(prompt, lower_bound, upper_bound)
    if lower_bound is not None:
        if value < lower_bound:
            print "TOO LOW"
            return ask_numeric(prompt, lower_bound, upper_bound)
    if upper_bound is not None:
        if value > upper_bound:
            print "TOO HIGH"
            return ask_numeric(prompt, lower_bound, upper_bound)
    return value


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

    if inv.get_money() < 0:
        print "YOU OVERSPENT--YOU ONLY HAD $700 TO SPEND.  BUY AGAIN"
        return initial_purchases()

    inv.set_oxen(oxen_spend)
    inv.set_food(food_spend)
    inv.set_bullets(ammunition_spend)
    inv.set_clothing(clothing_spend)
    inv.set_misc(misc_spend)

    print "AFTER ALL YOUR PURCHASES, YOU NOW HAVE", inv.get_money(), "DOLLARS LEFT"
    return inv

# TODO functions
# def fortStop():
# def hunting():
# def eat:
# def ridersAttack():
# def eventSelection():
# def mountains():
# def dying():
# def finalTurn():
# def shooting():
# def illness():

def next_fort():
    return


# hat tip: http://stackoverflow.com/questions/3471461/raw-input-and-timeout/3911560#3911560
def read_input_with_timeout(caption, timeout=7):
    start_time = time()
    stdout.write('%s ' % caption)
    response = ''
    entry_time = timeout
    while True:
        if kbhit():
            char = getche()
            if ord(char) == 13:  # enter key
                entry_time = time() - start_time
                break
            elif ord(char) >= 32:  # space char
                response += char
        if len(response) == 0 and (time() - start_time) > timeout:
            break

    print ''  # needed to move to next line
    return response, entry_time


# TODO: Windows only for now
def hunt(inv, track):
    if inv.get_bullets() < 40:
        print "TOUGH---YOU NEED MORE BULLETS TO GO HUNTING"
        return
    track.subtract_mileage(45)

    response, entry_time = read_input_with_timeout("TYPE BANG", 7)
    # debug logging? print "User typed", response, "after", entry_time, "seconds"

    # if the user didn't type bang, set the response time to the timeout value
    # for a likely miss
    if response.lower() != 'bang':
        entry_time = 7

    if entry_time < 1.0:
        print "RI\aGHT BETWEE\aN THE EYE\a'S---YOU GOT A\a BIG ONE!!\a!!"
        inv.add_food(52 + random() * 6)
        inv.subtract_bullets(10 - random() * 4)
    elif (100 * random()) < (13 * entry_time):
        print "SORRY---NO LUCK TODAY"
    else:
        print "NICE SHOT--RIGHT THROUGH THE NECK--FEAST TONIGHT!!"
        inv.add_food(48 - 2 * entry_time)
        inv.subtract_bullets(10 - 3 * entry_time)

    # Linux version?
    # def timeout():
    #     response = None
    #     _exit(1)

    # t = Timer(7, interrupt_main )
    # response = None
    # try:
    #    t.start()
    #     response = str(raw_input("TYPE BANG ")).lower().strip()
    # except KeyboardInterrupt:
    #     pass
    # t.cancel()

    # print response
    return

if __name__ == "__main__":

    if ask_yes_no("DO YOU NEED INSTRUCTIONS  (YES/NO)"):
        print_instructions()

    # initial purchases generate an inventory
    inventory = initial_purchases()

    # TODO Implement a Windows only module to use winsound to print bells, use this everywhere else?
    print "\a"

    calendar = Calendar()
    tracker = TripTracker()

    while not calendar.is_final_turn():
        calendar.print_date()
        inventory.print_warnings()
        tracker.print_mileage()
        inventory.print_inventory()
        turn_response = ask_numeric("DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT, \nOR (3) CONTINUE", 1, 3)
        if turn_response == 1:
            next_fort()
        elif turn_response == 2:
            hunt(inventory, tracker)

        # eating
        # TODO: If food less than 13, you're dead, otherwise prompt for eating style

        # do stuff
        # TODO: handle last turn mileage
        tracker.random_advance(inventory.get_oxen())
        calendar.advance_date()

    # TODO: Dead, your trip took too long
