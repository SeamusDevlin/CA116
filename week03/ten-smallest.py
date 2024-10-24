#!/usr/bin/env python3

smallest = int(input())
i = 0
while i < 9:
    n = int(input())
    a = n
    if a > smallest:
        smallest = smallest
        i = i + 1
    else:
        smallest = a
        i = i + 1
print(smallest)
