#!/usr/bin/env python3

s = input()
prefix = ""

if s[0] == "-":
    prefix = "-"
    s = s[1:]

i = 0
while i < len(s) and s[i] != ".":
    i = i + 1

if len(deciaml) == 0:
    decimal = "0"
   else:
    decimal = s
    fractional = "0"

print(prefix + decimal + "." + fractional)
