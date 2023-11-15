#!/usr/bin/env python3

total = 0

i = 0
while i < 10:
    n = int(input())
    total = total + n * (10 ** i)
    i = i + 1

i = 0
while i < 10:
    print(total // (10 ** (10 - i - 1)))
    total = total % (10 ** (10 - i - 1))
    i = i + 1
