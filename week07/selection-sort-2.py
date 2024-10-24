#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()

b = int(input())

p = b
while b < len(a):
    if int(a[b]) < int(a[p]):
        p = b
    b = b + 1

print(p)
