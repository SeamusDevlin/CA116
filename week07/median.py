#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()

i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1
    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp
    i = i + 1

print(a[len(a) // 2])
