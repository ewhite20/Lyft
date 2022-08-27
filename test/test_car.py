import unittest
from datetime import datetime
from engine.engines import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery.batteries import SpindlerBattery, NubbinBattery
from tire.tires import CarriganTire, OctoprimeTire


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):

    def test_needs_service_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today, )
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today, )
        self.assertFalse(battery.needs_service())


class TestCarriganTire(unittest.TestCase):
    def test_needs_service(self):
        wear = ([0, 0, 4, 0])
        tire = CarriganTire(wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear = ([0, 0, 0, 0.3])
        tire = CarriganTire(wear)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service(self):
        wear = ([0, 0, 4, 0])
        tire = OctoprimeTire(wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear = ([0, 0.2, 1, 1])
        tire = OctoprimeTire(wear)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
