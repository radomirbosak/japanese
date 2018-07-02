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

def test_27():
    assert number(27) == 'にじゅうなな'


def test_40():
    assert number(40) == 'よんじゅう'


def test_99():
    assert number(99) == 'きゅうじゅうきゅう'
