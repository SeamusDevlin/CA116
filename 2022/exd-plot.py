#!/usr/bin/env python3

import sys

n = sys.stdin.readline().strip()

a = sys.stdin.readline().strip()
plot = [" "] * n

i = 0
while i < len(n):
    pos = n[i]
    if 0 <= a < n:
        plot[a] = "*"
    i = i + 1

joinplot = "|" + "".join(plot) + "|"

print(joinplot)
