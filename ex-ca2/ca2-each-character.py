#!/usr/bin/env python3

import sys

with open("characters.txt", "r") as f:
    content = f.read()

ch = "\n"

i = 0
while i < len(content):
    j = 0
    while j < len(content[i]):
        if content[i][j] == ch:
            print(ch.strip())
        else:
            print(content[i][j])
        j = j + 1
    i = i + 1
