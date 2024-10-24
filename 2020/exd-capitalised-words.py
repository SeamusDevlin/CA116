#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split()

i = 0
while i < len(lines):
    if lines[i][0] >= "A" and lines[i][0] <= "Z":
        print(lines[i])
    i = i + 1
