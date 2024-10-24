#!/usr/bin/env python3

a = input()
b = input()
c = input()

if len(b) < len(a) > len(c):
   print(a)
elif len(a) < len(c) > len(b):
   print(c)
else:
   print(b)
