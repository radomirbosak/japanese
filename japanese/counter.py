

_zero = 'ぜろ'
_one = 'いち'
_ten = 'じゅう'
_hundred = 'ひゃく'
_thousand = 'せん'
_man = 'まん'


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

_replacements = {
    # 100
    'さんひゃく': 'さんびゃく',
    'ろくひゃく': 'ろっぴゃく',
    'はちひゃく': 'はっぴゃく',
    # 1000
    'さんせん': 'さんぜん',
    'はちせん': 'はっせん',
}


_orders = [
    (10000, _man),
    (1000, _thousand),
    (100, _hundred),
    (10, _ten),
]

def _compose_higher_part(num, word):
    if num == 1:
        return word

    naive_answer = number(num) + word
    return _apply_end_replacement(naive_answer)


def _apply_end_replacement(word):
    for src, dst in _replacements.items():
        if word.endswith(src):
            return word[:-len(src)] + dst

    return word

def _number_nozero(num):
    if num == 0:
        return ''

    if num == 1:
        return _one

    for order, order_word in _orders:
        if num < order:
            continue

        units, rest = divmod(num, order)
        higher_part = _compose_higher_part(units, order_word)
        return higher_part + _number_nozero(rest)

    return _single_digits[num]


def number(num):
    if num < 0:
        raise ValueError("Negative numbers are not supported.")
    if num >= 10000**2:
        raise ValueError("Numbers larger than 10^8 are not supported.")

    if num == 0:
        return _zero

    return _number_nozero(num)
