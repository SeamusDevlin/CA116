#!/usr/bin/env python3

import sys

animal = {}
snap = []
word = sys.stdin.readline().strip()

while 0 < len(word):
    if word in animal:
        snap.append(word)
    else:
        animal[word] = "true"
    word = sys.stdin.readline().strip()

if snap != []:
    print("snap:", snap[0])
