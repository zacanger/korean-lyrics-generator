# korean-lyrics-generator

[![Support with PayPal](https://img.shields.io/badge/paypal-donate-yellow.png)](https://paypal.me/zacanger) [![Patreon](https://img.shields.io/badge/patreon-donate-yellow.svg)](https://www.patreon.com/zacanger) [![ko-fi](https://img.shields.io/badge/donate-KoFi-yellow.svg)](https://ko-fi.com/U7U2110VB)

--------

Experiment to generate realistic-sounding Korean lyrics

WIP. Original project: <https://github.com/baehyunsol/korean_saying_generator>

## Installation

Clone it

## Usage

`./gen.py pattern-file`

`pattern-file` should contain a list of newline-delineated integers representing
the amount of syllables you want in each line of the resultant lyrics. Example
(from the first verse of [Butterfly by
LOONA](https://www.youtube.com/watch?v=XEOCbFJjRw0)):

```
5
7
6
5
7
5

8
8
9
8
8
```

## TODO:

Syllable count map

[LICENSE](./LICENSE.md)
