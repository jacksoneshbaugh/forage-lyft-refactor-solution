__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

from datetime import date, timedelta
from battery import Battery


class SpindlerBattery(Battery):

    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        """
        Checks if the battery requires servicing. Spindler batteries require
        servicing every 2 years
        :return: True if the battery needs servicing, false otherwise.
        """
        delta: timedelta = self.current_date - self.last_service_date
        return delta.days > 720
