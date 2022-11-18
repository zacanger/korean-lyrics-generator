#!/usr/bin/env python

import sys
import logic


def get_input():
    if len(sys.argv) != 2:
        print("Usage: generate.py pattern-file")
        sys.exit(0)
    with open(sys.argv[1], "r") as pattern_file:
        lines = pattern_file.readlines()
        return lines


def main():
    syllable_pattern = logic.get_patterns(get_input())
    results = logic.replace_pattern(syllable_pattern)
    print(results)


if __name__ == "__main__":
    main()
