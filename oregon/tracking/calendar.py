from datetime import date
from datetime import timedelta


# The DOW and year will be hardcoded, we advance two
# weeks through Mondays between March 29th and November 22nd
class Calendar(object):
    def advance_date(self):
        self._date += timedelta(days=14)
        self.turn_count += 1

    def rollback_date(self, rollback_days):
        self._date -= timedelta(days=rollback_days)

    def print_date(self):
        print("")
        print(self._date.strftime("Monday %B %d 1847"))
        print("")

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
