# korean-lyrics-generator

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

[LICENSE](./LICENSE.md)
