#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()
s = ["banana", "cherry", "orange", "pear", "apple"]
fruit = {}

i = 0
while i < len(s):
    fruit[s[i]] = True
    i = i + 1

i = 0
while i < len(words):
    if words[i] in fruit:
        print(words[i])
    i = i + 1
