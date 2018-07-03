

_zero = 'ぜろ'
_one = 'いち'
_ten = 'じゅう'
_hundred = 'ひゃく'


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


def _get_hundred_part(units):
    exceptions = {
        1: 'ひゃく',
        3: 'さんびゃく',
        6: 'ろっぴゃく',
        8: 'はっぴゃく',
    }

    if units in exceptions:
        return exceptions[units]

    return number(units) + _hundred


def _number_nozero(num):
    if num == 0:
        return ''

    if num == 1:
        return _one

    if num < 10:
        return _single_digits[num]

    if num < 100:
        units, rest = divmod(num, 10)
        return _single_digits[units] + _ten + _single_digits[rest]

    if num < 1000:
        units, rest = divmod(num, 100)
        return _get_hundred_part(units) + _number_nozero(rest)


def number(num):
    if num < 0:
        raise ValueError("Negative numbers are not supported.")
    if num > 999:
        raise ValueError("Numbers larger than 999 are not supported.")

    if num == 0:
        return _zero

    return _number_nozero(num)
