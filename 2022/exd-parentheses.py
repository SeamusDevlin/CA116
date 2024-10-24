#!/usr/bin/env python3

import sys

line = sys.stdin.readline()

i = 0
while i < len(line):
    j = 0
    while j < len(line[i]):
        char = line[i][j]
        if char == '(':
            start = char[i]
        elif char == ')' and start != -1:
            end = char[i]
        j = j + 1
    print(line[start + 1:end])
    line = sys.stdin.readline()
    i = i + 1

