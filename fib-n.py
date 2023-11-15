#!/usr/bin/env python3

n = int(input())

previous = 0
current = 1
fib_n = 0

i = 0
while i < n:
   print(fib_n)
   previous = current
   current = fib_n
   fib_n = previous + current
   i = i + 1
