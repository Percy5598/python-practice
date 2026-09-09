from calculator import subtract
def test_subtract_positive():
    assert subtract(10, 3) == 7


def test_subtract_zero():
    assert subtract(10, 0) == 10


def test_subtract_negative():
    assert subtract(-5, 2) == -7