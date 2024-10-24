#!/usr/bin/env python3

import sys

args = sys.argv[1:]
total = 0

i = 0
while i < len(args):
    with open(args[i]) as f:
        a = f.readlines()
        j = 0
        while j < len(a):
            b = a[j].strip().split()
            k = 0
            while k < len(b):
                value = int(b[k])
                total = total + value
                k = k + 1
            j = j + 1
    i = i + 1

print(total)
