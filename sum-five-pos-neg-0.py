#!/usr/bin/env python3

t1 = 0
t2 = 0
n = int(input())

while n != 0:
    if n < 0:
        t1 = t1 + n
    else:
        t2 = t2 + n
    n = int(input())
print(t1, t2)
