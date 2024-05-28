__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

import abc


class Battery(metaclass=abc.ABCMeta):
    """
    Represents a battery in a car in the Lyft rental fleet.
    """

    @classmethod
    def __subclasshook__(cls, __subclass):
        return hasattr(__subclass, 'needs_service') and callable(__subclass.needs_service)
