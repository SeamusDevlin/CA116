#!/usr/bin/env python3

import sys

word = sys.stdin.read().split()

i = 0
while i < len(word):
    name = word[i] + " " + word[i + 1]
    mark = int(word[i + 2])
    if mark >= 40:
        print(name)
    i = i + 3
