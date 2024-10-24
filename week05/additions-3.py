#!/usr/bin/env python3

while sum != 1000:
    n = input()
    i = 0
    while i < len(n) and n[i] != "+":
        i = i + 1
    ls = n[:i]
    rs = n[i + 1:]
    sum = int(ls) + int(rs)
    print(sum)
