#!/usr/bin/env python3

t1 = 0
t2 = 0

i = 0
while i < 5:
    n = int(input())
    if n < 0:
        t1 = t1 + n
    else:
        t2 = t2 + n
    i = i + 1

print(t1, t2)
