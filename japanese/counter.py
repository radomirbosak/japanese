

_zero = 'ぜろ'
_one = 'いち'
_ten = 'じゅう'


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


def number(num):
    if num < 0:
        raise ValueError("Negative numbers are not supported.")
    if num >= 100:
        raise ValueError("Numbers larger than 99 are not supported.")

    if num == 0:
        return _zero
    if num == 1:
        return _one
    if num < 10:
        return _single_digits[num]

    units, rest = divmod(num, 10)

    return _single_digits[units] + _ten + _single_digits[rest]
