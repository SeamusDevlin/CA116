#!/usr/bin/env python3

n = int(input())
a = ((n // 100) % 100) % 10 * 10 + ((n // 100) % 100) // 10
print(a)
