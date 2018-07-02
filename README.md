# Japanese

This repo contains functions useful for processing of Japanese text.

## Usage

### `japanese.string` module

The character ranges were taken from http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/ .

```python
>>> from japanese.string import hiragana, katakana, kanji

>>> hiragana
'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴ ふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ゙゚゛゜ゝゞゟ'

>>> katakana
'゠ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビ ピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿ'

>>> kanji[:10]
'㐀㐁㐂㐃㐄㐅㐆㐇㐈㐉'

>>> len(kanji)
27885
```

## Todo

* [x] string containing all hiragana characters
* [x] string containing all katakana characters
* [x] string containing all kanji characters
* [ ] functions for various counters
