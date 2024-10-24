#!/usr/bin/env python3

import sys

n = sys.stdin.readlines()
total = 0

i = 0
while i < len(n):
    total = total + int(n[i])
    i = i + 1

print(total)
