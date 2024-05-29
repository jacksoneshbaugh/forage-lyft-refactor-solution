__author__ = 'Jackson Eshbaugh'
__version__ = '05/29/2024'

from array import array
from tires import Tires


class CarriganTires(Tires):

    def __init__(self, wear_data: array[int]):
        self.wear_data = wear_data

    def needs_service(self) -> bool:
        """
        Determines whether these tires need servicing. Carrigan tires require servicing only when one or more of the
        values from the tire wear sensors are >= 0.9.
        :return: True if the tires need servicing, False otherwise
        """

        for data in self.wear_data:
            if data >= 0.9:
                return True
        return False
