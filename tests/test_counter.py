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


def test_100():
    assert number(100) == 'ひゃく'


def test_310():
    assert number(310) == 'さんびゃくじゅう'


def test_601():
    assert number(601) == 'ろっぴゃくいち'


def test_845():
    assert number(845) == 'はっぴゃくよんじゅうご'


def test_1000():
    assert number(1000) == 'せん'


def test_3010():
    assert number(3010) == 'さんぜんじゅう'


def test_8007():
    assert number(8007) == 'はっせんなな'


def test_10000():
    assert number(10000) == 'まん'


def test_88888888():
    assert number(88888888) == ('はっせんはっぴゃくはちじゅうはちまん'
                                'はっせんはっぴゃくはちじゅうはち')
