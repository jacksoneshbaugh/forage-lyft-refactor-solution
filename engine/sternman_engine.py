from abc import ABC

from engine import engine
from car import Car


class SternmanEngine(engine.Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        """
        Checks if this engine needs servicing.
        :return: True if this engine requires service, otherwise false
        """
        return self.warning_light_on
