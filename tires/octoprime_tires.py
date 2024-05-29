__author__ = 'Jackson Eshbaugh'
__version__ = '05/29/2024'

from array import array
from tires import Tires


class OctoprimeTires(Tires):

    def __init__(self, wear_data: array[int]):
        self.wear_data = wear_data

    def needs_service(self) -> bool:
        """
        Determines whether these tires need servicing. Octoprime tires require servicing only when the sum of
        all values returned by the wear sensors is >= 3.
        :return: True if the tires need servicing, False otherwise
        """

        return self.wear_data[0] + self.wear_data[1] + self.wear_data[2] + self.wear_data[3] >= 3
