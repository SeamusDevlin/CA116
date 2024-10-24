#!/usr/bin/env python3

n = int(input())

i = 0
while i < 5:
    a = int(input())
    if a == n:
        n = a
        print("equal")
    elif a < n:
        n = a
        print("lower")
    elif a > n:
        n = a
        print("higher")
    i = i + 1
