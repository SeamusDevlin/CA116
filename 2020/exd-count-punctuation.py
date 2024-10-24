#!/usr/bin/env python3

import sys

lines = sys.stdin.read()
punc = [".", "!", "?", ","]
total = 0

i = 0
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] in punc:
            total = total + 1
        j = j + 1
    i = i + 1

print(total)
