__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

import serviceable
from datetime import date

from battery import Battery, NubbinBattery, SpindlerBattery
from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine


class Car(serviceable.Serviceable):
    """
    Represents a car in the Lyft rental fleet
    :param engine: the car's engine
    :param battery: the car's battery
    """
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
        pass

    def needs_service(self) -> bool:
        """
        Checks if this car needs servicing.
        :return: True if this car requires service, otherwise false
        """

        return self.engine.needs_service() and self.battery.needs_service()

        pass

class CarFactory():
    def create_caliope(self, current_date: date, last_service_date: date, current_milage: int, last_service_mileage: int) -> Car:
        """
        Creates a Caliope car
        :param current_date: the current date
        :param last_service_date: the last date the car was serviced
        :param current_milage: the car's current milage
        :param last_service_mileage: the car's milage the last time it was serviced
        :return: a Caliope car
        """
        return Car(CapuletEngine(current_milage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def create_glissade(self, current_date: date, last_service_date: date, current_milage: int, last_service_mileage: int) -> Car:
        """
        Creates a Glissade car
        :param current_date: the current date
        :param last_service_date: the last date the car was serviced
        :param current_milage: the car's current milage
        :param last_service_mileage: the car's milage the last time it was serviced
        :return: a Glissade car
        """
        return Car(WilloughbyEngine(current_milage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        """
        Creates a Palindrome car
        :param current_date: the current date
        :param last_service_date: the last date the car was serviced
        :param warning_light_on: whether the car's check engine light is on
        :return: a Palindrome car
        """
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

    def create_rorschach(self, current_date: date, last_service_date: date, current_milage: int, last_service_mileage: int) -> Car:
        """
        Creates a Rorschach car
        :param current_date: the current date
        :param last_service_date: the last date the car was serviced
        :param current_milage: the car's current milage
        :param last_service_mileage: the car's milage the last time it was serviced
        :return: a Rorschach car
        """
        return Car(WilloughbyEngine(current_milage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date))

    def create_thovex(self, current_date: date, last_service_date: date, current_milage: int, last_service_mileage: int) -> Car:
        """
        Creates a Thovex car
        :param current_date: the current date
        :param last_service_date: the last date the car was serviced
        :param current_milage: the car's current milage
        :param last_service_mileage: the car's milage the last time it was serviced
        :return: a Thovex car
        """
        return Car(CapuletEngine(current_milage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date))
