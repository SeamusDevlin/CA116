#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
result = a * (c % 2 == 0) + b * (c % 2 != 0)
print(result)
