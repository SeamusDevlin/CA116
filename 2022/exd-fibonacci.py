#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline())
a, b = 0, 1

while a < n:
    a, b = b, b + a

if a == n and n >= 0:
    print("yes")

else:
    print("no")
