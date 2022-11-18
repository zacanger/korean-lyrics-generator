# korean-lyrics-generator

[![Support with PayPal](https://img.shields.io/badge/paypal-donate-yellow.png)](https://paypal.me/zacanger) [![Patreon](https://img.shields.io/badge/patreon-donate-yellow.svg)](https://www.patreon.com/zacanger) [![ko-fi](https://img.shields.io/badge/donate-KoFi-yellow.svg)](https://ko-fi.com/U7U2110VB)

--------

Experiment to generate realistic-sounding Korean lyrics. For use by songwriters
who don't speak much Korean. Not intended to produce actual quality lyrics, just
correct-ish series of syllables in the desired patterns. Originally based on
[this code](https://github.com/baehyunsol/korean_saying_generator).

## Usage

Go to `https://zacanger.com/korean-lyrics-generator`, or use the CLI (first
clone or download this repo) with `./cli.py pattern-file`.

`pattern-file` should contain a list of newline-delineated integers representing
the amount of syllables you want in each line of the resultant lyrics. Example:

```
# verse
5
7
6
5
7
5

# pre
8
0
9
8
8
```

The `0` represents a line you wish to be a repetition of the previous line.
Lines beginning with `#` are comments (these only work on their own line!).

## TODO

* Fix so lines aren't starting with particles or whatever

[LICENSE](./LICENSE.md)
