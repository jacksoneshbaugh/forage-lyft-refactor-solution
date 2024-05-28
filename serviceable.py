__author__ = 'Jackson Eshbaugh'
__version__ = '05/28/2024'

import abc


class Serviceable(metaclass=abc.ABCMeta):
    """
    An interface that represents any object in the Lyft rental system that requires service at some point.
    """
    @classmethod
    def __subclasshook__(cls, __subclass):
        return hasattr(__subclass, 'needs_service') and callable(__subclass.needs_service)
