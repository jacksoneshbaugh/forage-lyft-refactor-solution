from abc import ABC, abstractmethod

import serviceable


class Car(serviceable.Serviceable):
    def __init__(self, engine: Engine, battery: Batter):
        pass

    def needs_service(self) -> bool:
        """
        Checks if this car needs servicing.
        :return: True if this car requires service, otherwise false
        """

        return self.engine.needs_service() and self.battery.needs_service()

        pass
