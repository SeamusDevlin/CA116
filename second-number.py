#!/usr/bin/env python3

s = input()

i = 1
while i < len(s) and not("0" <= s[i] and s[i] <= "9"):
    i = i + 1


