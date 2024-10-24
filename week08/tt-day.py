#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    tokens = s.split()
    a.append(tokens)
    s = input()

d = int(input())

i = 0
while i < len(a):
    if d == int(a[i][0]):
        print(" ".join(a[i]))
    i = i + 1
