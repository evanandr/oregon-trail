from unittest import TestCase
from oregon import Health


class TestHealth(TestCase):
    def test_construction(self):
        health = Health()
        self.assertFalse(health.illness)
        self.assertFalse(health.injured)

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
