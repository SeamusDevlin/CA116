#!/usr/bin/env python3

s = input()

while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1
    a = s[i - 4:i]
    b = s[:i]
    if a == "City" and len(a) < len(b):
        print(b)

    s = input()
