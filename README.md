# korean-lyrics-generator

## WIP

See generate.py for todos. Also, maybe convert to JS and make it a webapp? Or
one of the libraries that transpiles Python to run in the browser?

[![Support with PayPal](https://img.shields.io/badge/paypal-donate-yellow.png)](https://paypal.me/zacanger) [![Patreon](https://img.shields.io/badge/patreon-donate-yellow.svg)](https://www.patreon.com/zacanger) [![ko-fi](https://img.shields.io/badge/donate-KoFi-yellow.svg)](https://ko-fi.com/U7U2110VB)

--------

Experiment to generate realistic-sounding Korean lyrics. For use by songwriters
who don't speak much Korean. Not intended to produce actual quality lyrics, just
correct-ish series of syllables in the desired patterns. Originally based on
[this code](https://github.com/baehyunsol/korean_saying_generator).

## Installation

Clone or download the project, and have Python installed.

## Usage

`./generate.py pattern-file`

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

## TODO

* Future thoughts: fix so lines aren't starting with particles or whatever
* Also maybe convert to a webapp?

[LICENSE](./LICENSE.md)
