#!/usr/bin/python
from datetime import date
from datetime import timedelta
from random import random
from sys import stdout
from time import time
from time import sleep
from msvcrt import kbhit, getche


class TripTracker(object):
    def random_advance(self, oxen):
        self.last_advance = 200 + (oxen.value - 220) / 5 + 10 * random()
        self._mileage += self.last_advance
        self._mileage = int(self._mileage)

    # this function should only be used for increases in mileage
    # during a turn
    def add_mileage(self, gained_ground):
        self.last_advance += gained_ground
        self._mileage += int(gained_ground)

    def subtract_mileage(self, lost_ground):
        self._mileage -= int(lost_ground)
        if self._mileage < 0:
            self._mileage = 0

    def print_mileage(self):
        print "TOTAL MILEAGE IS", self.mileage

    def reached_mountains(self):
        if self._mileage >= self._DISTANCE_TO_MOUNTAINS:
            return True
        return False

    def reached_oregon(self):
        if self._mileage >= self._TOTAL_TRIP_DISTANCE:
            try:
                self._last_turn_fraction = (self._TOTAL_TRIP_DISTANCE - self.last_advance) /\
                                           (self._mileage - self.last_advance)
            except ZeroDivisionError:
                self._last_turn_fraction = 0
            return True
        return False

    @property
    def mileage(self):
        return self._mileage

    @property
    def last_turn_fraction(self):
        return self._last_turn_fraction

    @property
    def total_trip_distance(self):
        return self._TOTAL_TRIP_DISTANCE

    @property
    def distance_to_mountains(self):
        return self._DISTANCE_TO_MOUNTAINS

    @property
    def cleared_south_pass(self):
        return self._cleared_south_pass

    @cleared_south_pass.setter
    def cleared_south_pass(self, value):
        self._cleared_south_pass = value

    @property
    def cleared_blue_mountains(self):
        return self._cleared_blue_mountains

    @cleared_blue_mountains.setter
    def cleared_blue_mountains(self, value):
        self._cleared_blue_mountains = value

    def __init__(self):
        self.last_advance = 0
        self._last_turn_fraction = 0
        self._mileage = 0
        self._TOTAL_TRIP_DISTANCE = 2040
        self._DISTANCE_TO_MOUNTAINS = 950
        self._cleared_south_pass = False
        self._cleared_blue_mountains = False


# The DOW and year will be hardcoded, we advance two
# weeks through Mondays between March 29th and November 22nd
class Calendar(object):
    def advance_date(self):
        self._date += timedelta(days=14)
        self.turn_count += 1

    def rollback_date(self, rollback_days):
        self._date -= timedelta(days=rollback_days)

    def print_date(self):
        print ""
        print self._date.strftime("Monday %B %d 1847")
        print ""

    def is_final_turn(self):
        if self.turn_count == self._TOTAL_TURN_COUNT:
            return True
        else:
            return False

    @property
    def date(self):
        return self._date

    @property
    def total_turn_count(self):
        return self._TOTAL_TURN_COUNT

    def __init__(self):
        self._date = date(2016, 3, 29)
        self.turn_count = 1
        self._TOTAL_TURN_COUNT = 18


# TODO: rename "TurnState"
class Health(object):
    @property
    def injured(self):
        return self._injured

    @injured.setter
    def injured(self, value):
        self._injured = value

    @property
    def illness(self):
        return self._ill

    @illness.setter
    def illness(self, value):
        self._ill = value

    @property
    def blizzard(self):
        return self._blizzard

    @blizzard.setter
    def blizzard(self, value):
        self._blizzard = value

    @property
    def eating_state(self):
        return self._eating_state

    @eating_state.setter
    def eating_state(self, value):
        if value < 1 or value > 3:
            self._eating_state = 0
        else:
            self._eating_state = value

    def eating_poorly(self):
        return self._eating_state == 1

    def eating_moderately(self):
        return self._eating_state == 2

    def eating_well(self):
        return self._eating_state == 3

    def __init__(self):
        self._injured = False
        self._ill = False
        self._blizzard = False
        self._eating_state = 0


class InventoryItem(object):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = int(value)

    def add(self, value):
        self._value += int(value)

    def subtract(self, value):
        self._value -= int(value)

    def __init__(self):
        self._value = 0


class Inventory(object):
    @property
    def money(self):
        return self._money

    def spend(self, cost):
        self._money -= int(cost)

    def print_warnings(self):
        if self.food.value < 12:
            print "YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!"

    def print_inventory(self):
        print '{0:8}|{1:9}|{2:10}|{3:14}|{4:6}|'.format("FOOD", " BULLETS ", " CLOTHING ", " MISC. SUPP. ", " CASH ")
        print '{0:7} |{1:8} |{2:9} |{3:13} |{4:5} |'.format(self.food.value, self.bullets.value, self.clothing.value,
                                                            self.misc.value, self._money)

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
        print "YOU OVERSPENT--YOU ONLY HAD $700 TO SPEND.  BUY AGAIN"
        return initial_purchases()

    inv.oxen.value = oxen_spend
    inv.food.value = food_spend
    inv.bullets.value = 50 * ammunition_spend
    inv.clothing.value = clothing_spend
    inv.misc.value = misc_spend

    print "AFTER ALL YOUR PURCHASES, YOU NOW HAVE", inv.money, "DOLLARS LEFT"
    return inv


def event_selection(inv, track, health):
    option = 0
    ranges = [6, 11, 13, 15, 17, 22, 32, 35, 37, 42, 44, 54, 64, 69, 95]
    random_number = 100 * random()
    for value in ranges:
        if random_number <= value:
            break
        option += 1

    if option == 0:  # wagon breaks down
        print "WAGON BREAKS DOWN--LOSE TIME AND SUPPLIES FIXING IT"
        track.subtract_mileage(15 + 5 * random())
        inv.misc.subtract(8)
        sleep(1)
    elif option == 1:  # ox injure leg
        print "OX INJURES LEG---SLOWS YOU DOWN REST OF TRIP"
        track.subtract_mileage(25)
        inv.oxen.subtract(20)
        sleep(1)
    elif option == 2:  # daughter breaks arm
        print "BAD LUCK---YOUR DAUGHTER BROKE HER ARM"
        print "YOU HAD TO STOP AND USE SUPPLIES TO MAKE A SLING"
        track.subtract_mileage(5 + 4 * random())
        inv.misc.subtract(2 + 3 * random())
        sleep(1)
    elif option == 3:  # ox wanders off
        print "OX WANDERS OFF---SPEND TIME LOOKING FOR IT"
        track.subtract_mileage(17)
        sleep(1)
    elif option == 4:  # son gets lost
        print "YOUR SON GETS LOST---SPEND HALF THE DAY LOOKING FOR HIM"
        track.subtract_mileage(10)
        sleep(1)
    elif option == 5:  # unsafe water
        print "UNSAFE WATER--LOSE TIME LOOKING FOR CLEAN SPRING"
        track.subtract_mileage((10 * random()) + 2)
        sleep(1)
    elif option == 6:  # heavy rains (mountains only)
        if track.reached_mountains():
            print "HEAVY RAINS---TIME AND SUPPLIES LOST"
            inv.food.subtract(10)
            inv.bullets.subtract(500)
            inv.misc.subtract(15)
            track.subtract_mileage((10 * random()) + 5)
            sleep(1)
    elif option == 7:  # bandits attack
        print "BANDITS ATTACK"
        sleep(1)
        response, entry_time = read_input_with_timeout("TYPE BANG", 7)
        inv.bullets.subtract(20 * entry_time)
        if inv.bullets.value <= 0:
            print "YOU RAN OUT OF BULLETS---THEY GET LOTS OF CASH"
            inv.spend(inv.money * 0.66)
        elif entry_time <= 1:
            print "QUICKEST DRAW OUTSIDE OF DODGE CITY!!!"
            print "YOU GOT 'EM!"
        else:
            print "YOU GOT SHOT IN THE LEG AND THEY TOOK ONE OF YOUR OXEN"
            print "BETTER HAVE A DOC LOOK AT YOUR WOUND"
            health.injured = True
            inv.misc.subtract(5)
            inv.oxen.subtract(20)
    elif option == 8:  # fire in the wagon
        print "THERE WAS A FIRE IN YOUR WAGON--FOOD AND SUPPLIES DAMAGED"
        inv.food.subtract(40)
        inv.bullets.subtract(400)
        inv.misc.subtract((random()*8) + 3)
        track.subtract_mileage(15)
        sleep(1)
    elif option == 9:  # heavy fog
        print "LOSE YOUR WAY IN HEAVY FOG---TIME IS LOST"
        track.subtract_mileage(10 + (5 * random()))
        sleep(1)
    elif option == 10:  # poisonous snake
        print "YOU KILLED A POISONOUS SNAKE AFTER IT BIT YOU"
        inv.bullets.subtract(10)
        inv.misc.subtract(5)
        sleep(1)
        if inv.misc.value <= 0:
            print "YOU DIE OF SNAKEBITE SINCE YOU HAVE NO MEDICINE"
            dying()
    elif option == 11:  # wagon swamped fording river
        print "WAGON GETS SWAMPED FORDING RIVER--LOSE FOOD AND CLOTHES"
        inv.food.subtract(30)
        inv.clothing.subtract(20)
        track.subtract_mileage(20 + (20 * random()))
        sleep(1)
    elif option == 12:  # wild animals attack
        print "WILD ANIMALS ATTACK!"
        sleep(1)
        response, entry_time = read_input_with_timeout("TYPE BANG", 7)
        if inv.bullets.value < 40:
            print "YOU WERE TOO LOW ON BULLETS--"
            print "THE WOLVES OVERPOWERED YOU"
            health.injured = True
        if entry_time <= 2:
            print "NICE SHOOTIN' PARDNER---THEY DIDN'T GET MUCH"
        else:
            print "SLOW ON THE DRAW---THEY GOT AT YOUR FOOD AND CLOTHES"
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
        print message
        sleep(1)
        if insufficient_clothing:
            illness(inv, track, health)
    elif option == 14:  # hail storm
        print "HAIL STORM---SUPPLIES DAMAGED"
        track.subtract_mileage(5 + (10 * random()))
        inv.bullets.subtract(200)
        inv.misc.subtract(4 + (3 * random()))
        sleep(1)
    elif option == 15:  # illness (based on eating choice)
        if health.eating_poorly():
            illness(inv, track, health)
        elif health.eating_moderately() and random() > 0.25:
            illness(inv, track, health)
        elif health.eating_well() and random() < 0.5:
            illness(inv, track, health)
        sleep(1)
    else:  # helpful indians
        print "HELPFUL INDIANS SHOW YOU WHERE TO FIND MORE FOOD"
        inv.food.add(14)
        sleep(1)


def mountains(inv, track, health):
    if not track.reached_mountains():
        return

    if (random() * 10) <= (9 - ((track.mileage / 100 - 15) ** 2 + 72) / ((track.mileage / 100 - 15) ** 2 + 12)):
        print "RUGGED MOUNTAINS"
        if random() <= 0.1:
            print "YOU GOT LOST---LOSE VALUABLE TIME TRYING TO FIND TRAIL!"
            track.subtract_mileage(60)
        elif random() <= 0.11:
            print "WAGON DAMAGED!---LOSE TIME AND SUPPLIES"
            track.subtract_mileage(20 + (30 * random()))
            inv.misc.subtract(5)
            inv.bullets.subtract(200)
        else:
            print "THE GOING GETS SLOW"
            track.subtract_mileage(45 + (random() / 0.02))

    # First pass evaluated at 950 miles (reached_mountains)
    if not track.cleared_south_pass:
        track.cleared_south_pass = True
        if random() < 0.8:
            blizzard(inv, track, health)
        else:
            print "YOU MADE IT SAFELY THROUGH SOUTH PASS--NO SNOW"

    # Second pass (blue mountains) at 1700 miles
    if track.mileage >= 1700 and not track.cleared_blue_mountains:
        track.cleared_blue_mountains = True
        if random() < 0.7:
            blizzard(inv, track, health)


def blizzard(inv, track, health):
    print "BLIZZARD IN MOUNTAIN PASS--TIME AND SUPPLIES LOST"
    inv.food.subtract(25)
    inv.misc.subtract(10)
    inv.bullets.subtract(300)
    track.subtract_mileage(30 + (40 * random()))
    if inv.clothing.value < (18 + (2 * random())):
        illness(inv, track, health)


def illness(inv, track, health):
    if (100 * random()) < (10 + (35 * health.eating_state - 1)):
        print "MILD ILLNESS---MEDICINE USED"
        track.subtract_mileage(5)
        inv.misc.subtract(2)
    elif (100 * random()) < (100 - (40 / (4 ** (health.eating_state - 1)))):
        print "BAD ILLNESS---MEDICINE USED"
        track.subtract_mileage(5)
        inv.misc.subtract(5)
    if inv.misc.value < 0:
        print "YOU RAN OUT MEDICAL SUPPLIES"
        message = "YOU DIED OF ";
        if health.injured:
            message += "INJURIES"
        else:
            message += "PNEUMONIA"
        print message
        dying()
    return


# The convoluted original logic for a rider attack: RND(0)*10>((M/100-4)^2+72)/((M/100-4)^2+12)-1
def do_riders_attack(track):
    return (random() * 10) > (((float(track.mileage) / 100.0 - 4) ** 2 + 72) /
                              ((float(track.mileage) / 100.0 - 4) ** 2 + 12) - 1)


def riders_attack(inv, track, health):
    peaceful = True
    if random() < 0.8:
        print "RIDERS AHEAD.  THEY DON'T LOOK HOSTILE"
    else:
        print "RIDERS AHEAD.  THEY LOOK HOSTILE"
        peaceful = False

    # riders may randomly switch sides
    if random() <= 0.2:
        peaceful = not peaceful

    print "TACTICS"
    print "(1) RUN  (2) ATTACK  (3) CONTINUE  (4) CIRCLE WAGONS"
    print "IF YOU RUN YOU'LL GAIN TIME BUT WEAR DOWN YOUR OXEN"
    response = ask_numeric("IF YOU CIRCLE YOU'LL LOSE TIME", 1, 4)
    if not peaceful:
        if response == 1:  # run
            track.add_mileage(20)
            inv.misc.subtract(15)
            inv.bullets.subtract(150)
            inv.oxen.subtract(40)
        elif response == 2:  # attack
            response, entry_time = read_input_with_timeout("TYPE BANG", 7)
            # Original bullet loss was "B=B-B1*40-80". This produces a gain in bullets
            # when response time is less than 2 seconds and small losses when the value is longer (max: 200)
            inv.bullets.subtract(entry_time * 28.57)
            if entry_time <= 1:
                print "NICE SHOOTING---YOU DROVE THEM OFF"
            elif entry_time <= 4:
                print "KINDA SLOW WITH YOUR COLT .45"
            else:
                print "LOUSY SHOT---YOU GOT KNIFED"
                print "YOU HAVE TO SEE OL' DOC BLANCHARD"
                health.injured = True
        elif response == 3:  # continue
            if random() <= 0.8:
                inv.misc.subtract(15)
                inv.bullets.subtract(150)
            else:
                print "THEY DID NOT ATTACK"
                return
        else:  # circle wagons
            response, entry_time = read_input_with_timeout("TYPE BANG", 7)
            inv.bullets.subtract((entry_time * 30) - 80)
            track.mileage.subtract(25)
            if entry_time <= 1:
                print "NICE SHOOTING---YOU DROVE THEM OFF"
            elif entry_time <= 4:
                print "KINDA SLOW WITH YOUR COLT .45"
            else:
                print "LOUSY SHOT---YOU GOT KNIFED"
                print "YOU HAVE TO SEE OL' DOC BLANCHARD"
                health.injured = True
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
        print "RIDERS WERE FRIENDLY, BUT CHECK FOR POSSIBLE LOSSES"
    else:
        print "RIDERS WERE HOSTILE--CHECK FOR LOSSES"
        if inv.bullets.value < 0:
            print "YOU RAN OUT OF BULLETS AND GOT MASSACRED BY THE RIDERS"
            dying()


def next_fort(inv, track):
    print "ENTER WHAT YOU WISH TO SPEND ON THE FOLLOWING"
    food = ask_numeric("FOOD", 0, inv.money)
    ammo = ask_numeric("AMMUNITION", 0, inv.money)
    clothing = ask_numeric("CLOTHING", 0, inv.money)
    misc = ask_numeric("MISCELLANEOUS SUPPLIES", 0, inv.money)
    total_spend = food + ammo + clothing + misc
    if inv.money < total_spend:
        print "YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN"
        return next_fort(inv, track)
    inv.spend(total_spend)
    inv.food.add(0.66 * food)
    inv.bullets.add(0.66 * ammo * 50)
    inv.clothing.add(0.66 * clothing)
    inv.misc.add(0.66*misc)
    track.subtract_mileage(45)


def eating(inv, health):
    response = ask_numeric("DO YOU WANT TO EAT (1) POORLY  (2) MODERATELY\nOR (3) WELL", 1, 3)
    food_eaten = 8 + 5 * response
    if inv.food.value < food_eaten:
        print "YOU CAN'T EAT THAT WELL"
        return eating(inv, health)
    health.eating_state = response
    inv.food.subtract(food_eaten)


def dying():
    print ""
    print "DO TO YOUR UNFORTUNATE SITUATION, THERE ARE A FEW"
    print "FORMALITIES WE MUST GO THROUGH"
    print ""
    # Responses to the first two questions are ignored intentionally
    ask_yes_no("WOULD YOU LIKE A MINISTER?")
    ask_yes_no("WOULD YOU LIKE A FANCY FUNERAL?")
    response = ask_yes_no("WOULD YOU LIKE US TO INFORM YOUR NEXT OF KIN?")
    if not response:
        print "YOUR AUNT NELLIE IN ST. LOUIS IS ANXIOUS TO HEAR"
    print ""
    print "WE THANK YOU FOR THIS INFORMATION AND WE ARE SORRY YOU"
    print "DIDN'T MAKE IT TO THE GREAT TERRITORY OF OREGON"
    print "BETTER LUCK NEXT TIME"
    print ""
    print ""
    print "                              SINCERELY"
    print "                 THE OREGON CITY CHAMBER OF COMMERCE"
    exit(0)


def completed_trip(inv, track, cal):
    print "YOU FINALLY ARRIVED AT OREGON CITY"
    print "AFTER", tracker.total_trip_distance, "LONG MILES---HOORAY!!!!!"

    cal.rollback_date(int(track.last_turn_fraction * 14))
    cal.print_date()
    inv.print_inventory()

    print "PRESIDENT JAMES K. POLK SENDS YOU HIS"
    print "      HEARTIEST CONGRATULATIONS"
    print ""
    print "           AND WISHES YOU A PROSPEROUS LIFE AHEAD"
    print ""
    print "                      AT YOUR NEW HOME"

# hat tip: http://stackoverflow.com/questions/3471461/raw-input-and-timeout/3911560#3911560
# TODO: Windows only for now, implement a linux version?
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


# TODO: refactor.  caption could be hard coded, bang response is fixed, rename this 'shoot'
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
    if response.lower() != 'bang':
        entry_time = timeout
    return response, entry_time


def hunt(inv, track):
    if inv.bullets.value < 40:
        print "TOUGH---YOU NEED MORE BULLETS TO GO HUNTING"
        return
    track.subtract_mileage(45)

    response, entry_time = read_input_with_timeout("TYPE BANG", 7)
    # debug logging? print "User typed", response, "after", entry_time, "seconds"

    if entry_time < 1.0:
        print "RI\aGHT BETWEE\aN THE EYE\a'S---YOU GOT A\a BIG ONE!!\a!!"
        inv.food.add(52 + random() * 6)
        inv.bullets.subtract(10 - random() * 4)
    elif (100 * random()) < (13 * entry_time):
        print "SORRY---NO LUCK TODAY"
    else:
        print "NICE SHOT--RIGHT THROUGH THE NECK--FEAST TONIGHT!!"
        inv.food.add(48 - 2 * entry_time)
        inv.bullets.subtract(10 - 3 * entry_time)


if __name__ == "__main__":

    if ask_yes_no("DO YOU NEED INSTRUCTIONS  (YES/NO)"):
        print_instructions()

    # initial purchases generate an inventory
    inventory = initial_purchases()

    calendar = Calendar()
    tracker = TripTracker()
    healthState = Health()

    while not calendar.is_final_turn() and not tracker.reached_oregon():
        calendar.print_date()
        inventory.zeroize_negative_values()

        # Resolve health issues from the previous turn
        if healthState.illness or healthState.injured:
            inventory.spend(20)
            if inventory.money < 0:
                print "YOU CAN'T AFFORD A DOCTOR"
                if healthState.illness:
                    print "YOU DIED OF PNEUMONIA"
                elif healthState.injured:
                    print "YOU DIED OF INJURIES"
                dying()
            else:
                print "DOCTOR'S BILL IS $20"
                healthState.illness = False
                healthState.injured = False

        # Show inventory status and mileage
        inventory.print_warnings()
        tracker.print_mileage()

        # Ask for turn options
        inventory.print_inventory()
        turn_response = ask_numeric("DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT, \nOR (3) CONTINUE", 1, 3)
        if turn_response == 1:
            next_fort(inventory, tracker)
        elif turn_response == 2:
            hunt(inventory, tracker)

        # Eating
        if inventory.food.value < 13:
            print "YOU RAN OUT OF FOOD AND STARVED TO DEATH"
            dying()
        eating(inventory, healthState)

        # Advance mileage now, events may subtract from overall
        # progress for each turn
        tracker.random_advance(inventory.oxen)

        # Rider attack
        if do_riders_attack(tracker):
            riders_attack(inventory, tracker, healthState)

        # Random per turn events
        event_selection(inventory, tracker, healthState)

        # Mountain events
        mountains(inventory, tracker, healthState)

        # Move to next turn
        calendar.advance_date()

    # Turns have been exhausted or Oregon has been reached
    if tracker.reached_oregon:
        completed_trip(inventory, tracker, calendar)
    else:
        print "TIME HAS RUN OUT.  WINTER HAS SET IN AND YOU DID NOT REACH OREGON."
        print "DISTANCE REMAINING: ", tracker.total_trip_distance - tracker.mileage
