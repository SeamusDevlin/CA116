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
        if int(a[j]) < int(a[p]):
            p = j
        j = j + 1
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    p = i
    i = i + 1

i = 0
while i < len(a):
    print(a[i])
    i = i + 1
