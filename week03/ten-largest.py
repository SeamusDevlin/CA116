#!/usr/bin/env python3

largest = int(input())
i = 0
while i < 9:
    n = int(input())
    a = n
    if a < largest:
        i = i + 1
    else:
        largest = a
        i = i + 1
print(largest)
