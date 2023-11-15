#!/usr/bin/env python3

n = int(input())
t = 0

if n != 0:
    a = int(input())
    while a != 0:
        if a < n:
            print("lower")
        elif n < a:
            print("higher")
        else:
            print("equal")
        n = a
        a = int(input())
else:
    t = 0
