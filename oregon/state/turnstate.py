class TurnState(object):
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
