from unittest import TestCase
from oregon import TripTracker
from oregon import InventoryItem


class TestTripTracker(TestCase):
    def test_construction(self):
        tracker = TripTracker()
        self.assertEqual(tracker.mileage, 0)
        self.assertEqual(tracker.last_turn_fraction, 0)
        self.assertEqual(tracker.total_trip_distance, 2040)
        self.assertEqual(tracker.distance_to_mountains, 950)
        self.assertFalse(tracker.cleared_south_pass)
        self.assertFalse(tracker.cleared_blue_mountains)

    def test_random_advance(self):
        tracker = TripTracker()
        oxen = InventoryItem()
        oxen.value = 220
        tracker.random_advance(oxen)
        self.assertGreaterEqual(tracker.mileage, 200)
        self.assertLess(tracker.mileage, 210)

    def test_add_mileage(self):
        tracker = TripTracker()
        tracker.add_mileage(10)
        self.assertEqual(tracker.mileage, 10)

    def test_subtract_mileage(self):
        tracker = TripTracker()
        tracker.add_mileage(10)
        self.assertEqual(tracker.mileage, 10)
        tracker.subtract_mileage(5)
        self.assertEqual(tracker.mileage, 5)

    def test_subtract_mileage_less_than_zero(self):
        tracker = TripTracker()
        tracker.subtract_mileage(10)
        self.assertEqual(tracker.mileage, 0)

    def test_reached_oregon(self):
        tracker = TripTracker()
        tracker.add_mileage(1800)
        oxen = InventoryItem()
        oxen.value = 220
        tracker.random_advance(oxen)  # maximum added advance of 210
        self.assertFalse(tracker.reached_oregon())
        last_turn_mileage = tracker.mileage - 1800
        last_turn_mileage += tracker.total_trip_distance - tracker.mileage
        tracker.add_mileage(tracker.total_trip_distance - tracker.mileage)
        self.assertTrue(tracker.reached_oregon())

    def test_reached_oregon_zero_division(self):
        tracker = TripTracker()
        tracker.add_mileage(tracker.total_trip_distance)
        self.assertTrue(tracker.reached_oregon())
        self.assertEqual(tracker.last_turn_fraction, 0)

    def test_reached_mountains(self):
        tracker = TripTracker()
        self.assertFalse(tracker.reached_mountains())
        tracker.add_mileage(tracker.distance_to_mountains)
        self.assertTrue(tracker.reached_mountains())
