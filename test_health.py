from unittest import TestCase
from oregon import TurnState


class TestHealth(TestCase):
    def test_construction(self):
        health = TurnState()
        self.assertFalse(health.illness)
        self.assertFalse(health.injured)
        self.assertEqual(health.eating_state, 0)

    def test_set_injured(self):
        health = TurnState()
        health.illness = True
        self.assertTrue(health.illness)
        health.illness = False
        self.assertFalse(health.illness)

    def test_set_illness(self):
        health = TurnState()
        health.injured = True
        self.assertTrue(health.injured)
        health.injured = False
        self.assertFalse(health.injured)

    def test_set_blizzard(self):
        health = TurnState()
        health.blizzard = True
        self.assertTrue(health.blizzard)
        health.blizzard = False
        self.assertFalse(health.blizzard)

    def test_eating_state_invalid(self):
        health = TurnState()
        health.eating_state = 4
        self.assertEqual(health.eating_state, 0)
        self.assertFalse(health.eating_poorly())
        self.assertFalse(health.eating_moderately())
        self.assertFalse(health.eating_well())

    def test_eating_state_poorly(self):
        health = TurnState()
        health.eating_state = 1
        self.assertEqual(health.eating_state, 1)
        self.assertTrue(health.eating_poorly())
        self.assertFalse(health.eating_moderately())
        self.assertFalse(health.eating_well())

    def test_eating_state_moderately(self):
        health = TurnState()
        health.eating_state = 2
        self.assertEqual(health.eating_state, 2)
        self.assertFalse(health.eating_poorly())
        self.assertTrue(health.eating_moderately())
        self.assertFalse(health.eating_well())

    def test_eating_state_well(self):
        health = TurnState()
        health.eating_state = 3
        self.assertEqual(health.eating_state, 3)
        self.assertFalse(health.eating_poorly())
        self.assertFalse(health.eating_moderately())
        self.assertTrue(health.eating_well())
