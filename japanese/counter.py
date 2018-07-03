

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

    if num < 10:
        return _single_digits[num]

    if num < 100:
        units, rest = divmod(num, 10)
        return _single_digits[units] + _ten + _single_digits[rest]

    if num < 1000:
        units, rest = divmod(num, 100)
        higher_part = _compose_higher_part(units, _hundred, _hundred_exceptions)
        return higher_part + _number_nozero(rest)

    if num < 10000:
        units, rest = divmod(num, 1000)
        higher_part = _compose_higher_part(units, _thousand, _thousand_exceptions)
        return higher_part + _number_nozero(rest)


def number(num):
    if num < 0:
        raise ValueError("Negative numbers are not supported.")
    if num > 9999:
        raise ValueError("Numbers larger than 9999 are not supported.")

    if num == 0:
        return _zero

    return _number_nozero(num)
