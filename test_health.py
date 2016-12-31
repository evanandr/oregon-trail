from unittest import TestCase
from oregon import Health


class TestHealth(TestCase):
    def test_construction(self):
        health = Health()
        self.assertFalse(health.illness)
        self.assertFalse(health.injured)
        self.assertEquals(health.eating_state, 0)

    def test_set_injured(self):
        health = Health()
        health.illness = True
        self.assertTrue(health.illness)
        health.illness = False
        self.assertFalse(health.illness)

    def test_set_illness(self):
        health = Health()
        health.injured = True
        self.assertTrue(health.injured)
        health.injured = False
        self.assertFalse(health.injured)

    def test_set_blizzard(self):
        health = Health()
        health.blizzard = True
        self.assertTrue(health.blizzard)
        health.blizzard = False
        self.assertFalse(health.blizzard)

    def test_eating_state_invalid(self):
        health = Health()
        health.eating_state = 4
        self.assertEquals(health.eating_state, 0)
        self.assertFalse(health.eating_poorly())
        self.assertFalse(health.eating_moderately())
        self.assertFalse(health.eating_well())

    def test_eating_state_poorly(self):
        health = Health()
        health.eating_state = 1
        self.assertEquals(health.eating_state, 1)
        self.assertTrue(health.eating_poorly())
        self.assertFalse(health.eating_moderately())
        self.assertFalse(health.eating_well())

    def test_eating_state_moderately(self):
        health = Health()
        health.eating_state = 2
        self.assertEquals(health.eating_state, 2)
        self.assertFalse(health.eating_poorly())
        self.assertTrue(health.eating_moderately())
        self.assertFalse(health.eating_well())

    def test_eating_state_well(self):
        health = Health()
        health.eating_state = 3
        self.assertEquals(health.eating_state, 3)
        self.assertFalse(health.eating_poorly())
        self.assertFalse(health.eating_moderately())
        self.assertTrue(health.eating_well())
