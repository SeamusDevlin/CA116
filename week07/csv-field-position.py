#!/usr/bin/env python3

import sys

t = sys.argv[1]
a = []

if __name__ == "__main__":
    s = "LatD,LatM,LatS,NS,LonD,LonM,LonS,EW,City,State"
else:
    s = input()

location = 0
i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] != ",":
        j = j + 1
    a.append(s[i:j])
    i = j + 1

i = 0
while i < len(a) and a[i] != t:
    i = i + 1

print(i)
