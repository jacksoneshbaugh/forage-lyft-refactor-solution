__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

from engine import engine


class WilloughbyEngine(engine.Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        """
        Checks if this engine needs servicing.
        :return: True if this engine requires service, otherwise false
        """
        return self.current_mileage - self.last_service_mileage > 60000
