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

### `japanese.counter` module

```python
>>> from japanese.counter import number

>>> number(10)
'じゅう'

>>> number(99)
'きゅうじゅうきゅう'

>>> number(845)
'はっぴゃくよんじゅうご'
```

## Todo

* [x] string containing all hiragana characters
* [x] string containing all katakana characters
* [x] string containing all kanji characters
* [ ] functions for various counters
	* [ ] plain numbers
		* [x] counting to 10
		* [x] counting to 99
		* [x] counting to 999
		* [ ] counting to 9999
		* [ ] counting to 99999999
		* [ ] counting to 999999999999
		* [ ] counting to 9999999999999999
		* [ ] counting to 99999999999999999999
	* [ ] days in week
	* [ ] days in month
	* [ ] months
	* [ ] years
	* [ ] hours
	* [ ] minutes
