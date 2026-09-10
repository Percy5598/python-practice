import pytest


@pytest.fixture
def sample_data():
    return [10, 20, 30]



def test_sum(sample_data):
    assert sum(sample_data) == 60    