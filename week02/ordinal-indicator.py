#!/usr/bin/env python3

n = int(input())
if n <= 0:
   print(n)
else:
   if 10 <= n % 100 <= 20:
      a = "th"
   else:
      last_digit = n % 10
      if last_digit == 1:
         a = "st"
      elif last_digit == 2:
         a = "nd"
      elif last_digit == 3:
         a = "rd"
      else:
         a = "th"
print(f"{a}")
