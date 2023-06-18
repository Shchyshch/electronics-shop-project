import pytest
from src.phone import Phone


@pytest.fixture
def test_phone():
    return Phone('Motorola C115', 1000, 10, 1)


def test__repr__(test_phone):
    assert repr(test_phone) == "Phone('Motorola C115', 1000, 10, 1)"


def test_number_of_sim(test_phone):
    test_phone.number_of_sim = 3
    assert test_phone.number_of_sim == 3
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 1.1
    with pytest.raises(ValueError):
        Phone('Nokia 3310', 1000, 10, -7)
