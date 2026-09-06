"""
__init__.py can act as the public interface of your package.

use this in __init__.py
from .calculator import add, multiply
from .statistics import mean

so user can do this
from math_tools import add, multiply, mean

"""

from .calculator import add, subtract, multiply, divide
from .statistics import mean, maximum, minimum