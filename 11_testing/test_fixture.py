
"""
pytest
  ↓
find test_total()
  ↓
see that it needs "numbers"
  ↓
run numbers fixture
  ↓
get [10, 20, 30]
  ↓
give it to test_total()
  ↓
run assertion
  ↓
PASS

It works as follows:
Finds the project/test files
Imports the test modules
Discovers functions beginning with test_
Finds fixtures required by those tests
Runs setup/fixtures
Executes the test
Evaluates assertions
Catches failures/exceptions
Reports the results

                 pytest
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
      find tests          find fixtures
          │                   │
          └─────────┬─────────┘
                    ↓
                run tests
                    ↓
              check assertions
                    ↓
             ┌──────┴──────┐
             ↓             ↓
           PASS           FAIL
"""     



def test_total():
    numbers = [10, 20, 30]
    assert sum(numbers) == 60

def test_length():
    numbers = [10, 20, 30]
    assert len(numbers) == 3

import pytest
@pytest.fixture
def numbers():
    return [10, 20, 30]


def test_total(numbers):
    assert sum(numbers) == 60


def test_length(numbers):
    assert len(numbers) == 3   
