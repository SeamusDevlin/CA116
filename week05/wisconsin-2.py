#!/usr/bin/env python3

s = input()
count = 0

while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1
    ls = s[i + 1:i + 3]
    if ls == "WI":
        count = count + 1

    s = input()
print(count)
