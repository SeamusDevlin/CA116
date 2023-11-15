#!/usr/bin/env python3

n = int(input())
leap = (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)
print(leap)
