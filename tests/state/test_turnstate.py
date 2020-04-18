from unittest import TestCase
from oregon.state.turnstate import TurnState


class TestTurnState(TestCase):
    def test_construction(self):
        turn_state = TurnState()
        self.assertFalse(turn_state.illness)
        self.assertFalse(turn_state.injured)
        self.assertEqual(turn_state.eating_state, 0)

    def test_set_injured(self):
        turn_state = TurnState()
        turn_state.illness = True
        self.assertTrue(turn_state.illness)
        turn_state.illness = False
        self.assertFalse(turn_state.illness)

    def test_set_illness(self):
        turn_state = TurnState()
        turn_state.injured = True
        self.assertTrue(turn_state.injured)
        turn_state.injured = False
        self.assertFalse(turn_state.injured)

    def test_set_blizzard(self):
        turn_state = TurnState()
        turn_state.blizzard = True
        self.assertTrue(turn_state.blizzard)
        turn_state.blizzard = False
        self.assertFalse(turn_state.blizzard)

    def test_eating_state_invalid(self):
        turn_state = TurnState()
        turn_state.eating_state = 4
        self.assertEqual(turn_state.eating_state, 0)
        self.assertFalse(turn_state.eating_poorly())
        self.assertFalse(turn_state.eating_moderately())
        self.assertFalse(turn_state.eating_well())

    def test_eating_state_poorly(self):
        turn_state = TurnState()
        turn_state.eating_state = 1
        self.assertEqual(turn_state.eating_state, 1)
        self.assertTrue(turn_state.eating_poorly())
        self.assertFalse(turn_state.eating_moderately())
        self.assertFalse(turn_state.eating_well())

    def test_eating_state_moderately(self):
        turn_state = TurnState()
        turn_state.eating_state = 2
        self.assertEqual(turn_state.eating_state, 2)
        self.assertFalse(turn_state.eating_poorly())
        self.assertTrue(turn_state.eating_moderately())
        self.assertFalse(turn_state.eating_well())

    def test_eating_state_well(self):
        turn_state = TurnState()
        turn_state.eating_state = 3
        self.assertEqual(turn_state.eating_state, 3)
        self.assertFalse(turn_state.eating_poorly())
        self.assertFalse(turn_state.eating_moderately())
        self.assertTrue(turn_state.eating_well())
