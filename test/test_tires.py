import unittest

from tires import CarriganTires, OctoprimeTires


class CarriganTiresTest(unittest.TestCase):
    def test_should_be_serviced(self):
        carrigan: CarriganTires = CarriganTires([0.254, 0.578, 0.888, 0.924])
        self.assertTrue(carrigan.needs_service())
        carrigan = CarriganTires([1, 0.925, 0.458, 0.261])
        self.assertTrue(carrigan.needs_service())

    def test_should_not_be_serviced(self):
        carrigan: CarriganTires = CarriganTires([0.254, 0.578, 0.888, 0.785])
        self.assertFalse(carrigan.needs_service())
        carrigan = CarriganTires([0.456, 0.146, 0.458, 0.261])
        self.assertFalse(carrigan.needs_service())


class OctoprimeTiresTest(unittest.TestCase):
    def test_should_be_serviced(self):
        octoprime: OctoprimeTires = OctoprimeTires([0.953, 0.578, 0.888, 0.924])
        self.assertTrue(octoprime.needs_service())
        octoprime = OctoprimeTires([1, 1, 0.674, 0.558])
        self.assertTrue(octoprime.needs_service())

    def test_should_not_be_serviced(self):
        octoprime: OctoprimeTires = OctoprimeTires([0.254, 0.578, 0.888, 0.785])
        self.assertFalse(octoprime.needs_service())
        octoprime = OctoprimeTires([0.456, 0.146, 0.458, 0.261])
        self.assertFalse(octoprime.needs_service())


if __name__ == '__main__':
    unittest.main()
