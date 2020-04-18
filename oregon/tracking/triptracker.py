from random import random


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
        print(("TOTAL MILEAGE IS", self.mileage))

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
