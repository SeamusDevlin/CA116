#!/usr/bin/env python3

s = input()

a = len(s) - 1
c = s[a]
b = s[0]
t = s[1:a]

print(c + t + b)
