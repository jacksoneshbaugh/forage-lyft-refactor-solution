__author__ = 'Jackson Eshbaugh'
__version__ = '05/29/2024'

import abc


class Tires(metaclass=abc.ABCMeta):
    """
    Represents the tires of a car in the Lyft rental fleet.
    """

    def __subclasshook__(cls, __subclass):
        return hasattr(__subclass, 'needs_service') and callable(__subclass.needs_service)
