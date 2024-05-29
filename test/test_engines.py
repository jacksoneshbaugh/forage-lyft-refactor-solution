__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

import unittest

from engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class CapuletEngineTest(unittest.TestCase):

    def test_should_be_serviced(self):
        capulet: CapuletEngine = CapuletEngine(30500, 0)
        self.assertTrue(capulet.needs_service())
        capulet = CapuletEngine(75000, 40000)
        self.assertTrue(capulet.needs_service())
        pass

    def test_should_not_be_serviced(self):
        capulet: CapuletEngine = CapuletEngine(15000, 0)
        self.assertFalse(capulet.needs_service())
        capulet = CapuletEngine(75000, 60000)
        self.assertFalse(capulet.needs_service())
        pass


class SternmanEngineTest(unittest.TestCase):

    def test_should_be_serviced(self):
        sternman: SternmanEngine = SternmanEngine(True)
        self.assertTrue(sternman.needs_service())
        pass

    def test_should_not_be_serviced(self):
        sternman: SternmanEngine = SternmanEngine(False)
        self.assertFalse(sternman.needs_service())
        pass


class WilloughbyEngineTest(unittest.TestCase):

    def test_should_be_serviced(self):
        willoughby: WilloughbyEngine = WilloughbyEngine(75005, 0)
        self.assertTrue(willoughby.needs_service())
        willoughby = WilloughbyEngine(80510, 20000)
        self.assertTrue(willoughby.needs_service())
        pass

    def test_should_not_be_serviced(self):
        willoughby: WilloughbyEngine = WilloughbyEngine(30000, 0)
        self.assertFalse(willoughby.needs_service())
        willoughby = WilloughbyEngine(80547, 60000)
        self.assertFalse(willoughby.needs_service())
        pass


if __name__ == '__main__':
    unittest.main()
