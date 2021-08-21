from .utils import *
from .errors import *
from typing import Union, Optional


class Quantity:
    __slots__ = ['_magnitude', '_unit']

    def __init__(self, magnitude: Union[int, float], unit: str):
        self._magnitude = magnitude
        self._unit = unit
        self._argscheck()

    def _argscheck(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __le__(self, other):
        pass

    @property
    def magnitude(self):
        return self._magnitude

    @magnitude.setter
    def magnitude(self, _magnitude):
        if not isinstance(_magnitude, (int, float)):
            raise TypeError(f"magnitude must of type 'int' or 'float'")
        self._magnitude = _magnitude

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, _unit):
        if not isinstance(_unit, str):
            raise TypeError(f"unit must be of type 'str'")
        self._unit = _unit

