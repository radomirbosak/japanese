import pytest

from japanese.counter import number


def test_zero():
    assert number(0) == 'ぜろ'


def test_four():
    assert number(4) == 'よん'


def test_ten():
    assert number(10) == 'じゅう'


def test_negative():
    with pytest.raises(ValueError):
        number(-5)
