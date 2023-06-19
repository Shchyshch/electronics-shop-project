import pytest
from src.keyboard import Keyboard


@pytest.fixture
def test_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test__str__(test_keyboard):
    assert str(test_keyboard) == "Dark Project KD87A"


def test_change_lang(test_keyboard):
    assert test_keyboard.language == "EN"
    test_keyboard.change_lang()
    assert test_keyboard.language == "RU"
    test_keyboard.change_lang().change_lang()
    assert test_keyboard.language == "RU"
    with pytest.raises(AttributeError):
        test_keyboard.language = 'FR'
    with pytest.raises(AttributeError):
        Keyboard('Dark Project KD87A', 9600, 5, 'FR')
