__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

from engine import engine


class SternmanEngine(engine.Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        """
        Checks if this engine needs servicing.
        :return: True if this engine requires service, otherwise false
        """
        return self.warning_light_on
