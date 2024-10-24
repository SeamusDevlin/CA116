#!/usr/bin/env python3

s = input()
a = [0] * 10

while s != "end":
    s = int(s)
    a[s] = a[s] + 1
    s = input()

i = 0
while i < 10:
    print(i, "*" * a[i])
    i = i + 1
