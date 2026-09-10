import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 20, 30),
        (-1, 1, 0),
        (100, 50, 150),
    ],
)

# Mocking

def test_add(a, b, expected):
    assert add(a, b) == expected


from unittest.mock import Mock

api = Mock()
api.get_price.return_value = 100

assert api.get_price("AAPL") == 100  

# Patch ()
from unittest.mock import patch

@patch("module.get_stock_price")
def test_stock_price(mock_price):
    mock_price.return_value = 100

    assert get_stock_price("AAPL") == 100


