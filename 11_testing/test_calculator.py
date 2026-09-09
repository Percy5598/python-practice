from calculator import subtract
from calculator import divide
from calculator import withdraw
import pytest
"""
From your project directory, 
Pytest starts looking through your project for tests.
by default it looks for:
test_something.py
test_*.py
*_test.py
"""

def test_subtract_positive():
    assert subtract(10, 3) == 7


def test_subtract_zero():
    assert subtract(10, 0) == 10


def test_subtract_negative():
    assert subtract(-5, 2) == -7

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_withdraw():
    assert withdraw(100, 30) == 70


def test_withdraw_too_much():
    with pytest.raises(ValueError):
        withdraw(100, 150)
   
def test_withdraw_too_much():
    with pytest.raises(ValueError, match="Insufficient balance"):
        withdraw(100, 150)   

