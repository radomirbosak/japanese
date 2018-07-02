

_zero = 'ぜろ'


_single_digits = [
    _zero,
    'いち',
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
    if num > 10:
        raise ValueError("Numbers larger than 10 are not supported.")

    return _single_digits[num]
