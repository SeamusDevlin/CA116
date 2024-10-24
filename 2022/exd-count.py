#!/usr/bin/env python3

import sys

args = int(sys.argv[1])

i = 0
while i < args:
    if args ** 0.5 > i:
        print(i)
    i = i + 1
