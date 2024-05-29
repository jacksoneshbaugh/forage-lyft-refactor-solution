__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

import unittest
from datetime import date

from battery import NubbinBattery, SpindlerBattery


class SpindlerBatteryTest(unittest.TestCase):

    def test_should_be_serviced(self):
        spindler: SpindlerBattery = SpindlerBattery(date(2023, 7, 13), date(2025, 8, 9))
        self.assertTrue(spindler.needs_service())
        spindler = SpindlerBattery(date(2021, 10, 31), date(2024, 11, 11))
        self.assertTrue(spindler.needs_service())
        pass

    def test_should_not_be_serviced(self):
        spindler: SpindlerBattery = SpindlerBattery(date(2023, 5, 28), date(2024, 5, 28))
        self.assertFalse(spindler.needs_service())
        spindler = SpindlerBattery(date(2022, 9, 18), date(2023, 12, 25))
        self.assertFalse(spindler.needs_service())
        pass


class NubbinBatteryTest(unittest.TestCase):

    def test_should_be_serviced(self):
        nubbin: NubbinBattery = NubbinBattery(date(2020, 1, 1), date(2024, 5, 28))
        self.assertTrue(nubbin.needs_service())
        nubbin = NubbinBattery(date(2018, 3, 17), date(2023, 6, 30))
        self.assertTrue(nubbin.needs_service())
        pass

    def test_should_not_be_serviced(self):
        nubbin: NubbinBattery = NubbinBattery(date(2022, 1, 1), date(2024, 5, 28))
        self.assertFalse(nubbin.needs_service())
        nubbin = NubbinBattery(date(2018, 3, 17), date(2019, 6, 30))
        self.assertFalse(nubbin.needs_service())
        pass


if __name__ == '__main__':
    unittest.main()
