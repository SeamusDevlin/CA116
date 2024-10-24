#!/usr/bin/env python3

a = int(input())

if a >= 2 and a % 2 == 0 and a - 2 != 0:
   print("not prime")
elif a >= 2 and a % 3 == 0 and a - 3 != 0:
   print("not prime")
elif a == 1:
   print("not prime")
else:
   print("prime")
