__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

from engine import engine


class CapuletEngine(engine.Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        """
        Checks if this engine needs servicing. Capulet engines require servicing every 30000 miles.
        :return: True if this engine requires service, otherwise false
        """
        return self.current_mileage - self.last_service_mileage > 30000
