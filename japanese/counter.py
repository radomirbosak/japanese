

_zero = 'ぜろ'
_one = 'いち'
_ten = 'じゅう'
_hundred = 'ひゃく'
_thousand = 'せん'


_single_digits = [
    '',
    '',
    'に',
    'さん',
    'よん',
    'ご',
    'ろく',
    'なな',
    'はち',
    'きゅう',
    'じゅう',
]

_hundred_exceptions = {
    3: 'さんびゃく',
    6: 'ろっぴゃく',
    8: 'はっぴゃく',
}

_thousand_exceptions = {
    3: 'さんぜん',
    8: 'はっせん',
}


_orders = [
    (1000, lambda x: _compose_higher_part(x, _thousand, _thousand_exceptions)),
    (100, lambda x: _compose_higher_part(x, _hundred, _hundred_exceptions)),
    (10, lambda x: _compose_higher_part(x, _ten)),
]

def _compose_higher_part(num, word, exceptions=None):
    if exceptions is None:
        exceptions = {}

    if num in exceptions:
        return exceptions[num]

    if num == 1:
        return word

    return number(num) + word


def _number_nozero(num):
    if num == 0:
        return ''

    if num == 1:
        return _one

    for order, compose_fn in _orders:
        if num < order:
            continue

        units, rest = divmod(num, order)
        return compose_fn(units) + _number_nozero(rest)

    return _single_digits[num]


def number(num):
    if num < 0:
        raise ValueError("Negative numbers are not supported.")
    if num > 9999:
        raise ValueError("Numbers larger than 9999 are not supported.")

    if num == 0:
        return _zero

    return _number_nozero(num)
