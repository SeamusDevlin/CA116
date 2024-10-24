#!/usr/bin/env python3


n = int(input())
x = 0
i = 0

print(x)
while i < (n - 1):
    x = -x + x % 2 * 2 - 1
    print(x)
    i = i + 1
